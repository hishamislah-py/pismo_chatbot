"""Adapter around the existing AI pipeline (pismo_assistant.pipeline.Assistant). No retrieval or generation logic lives
here: the backend only calls Assistant.answer(question) and maps its result.

The pipeline is synchronous and its first construction loads the index and embedding model (~10 s), so it is created
once, lazily (or at start-up when ASSISTANT_PRELOAD is true), and called in a worker thread with a timeout. Calls are
serialised with a lock: the demo pipeline is not documented as thread-safe.

Timing (see timing.py): the real pipeline is built with timing wrappers around its injectable retriever and generator,
so retrieval, LLM and the stages between them are measured without changing pismo_assistant. An injected pipeline
(tests) only gets load / lock-wait / pipeline totals unless a StageClock is passed too.

Streaming (streaming endpoint only, see streaming.py): when a call carries an observer, the generator asks the model to
stream the SAME prompt in the SAME JSON mode, forwards the provisional "answer" text as deltas, then parses the complete
output with pismo_assistant's own parse_output; the pipeline's citation validation runs on that result unchanged.
Calls without an observer (the regular endpoint) use the unchanged non-streamed request."""
import asyncio
import threading
import time
from typing import Any, Protocol

from .streaming import AnswerDeltas, CallObserver
from .timing import StageClock, TimedGenerator, TimedRetriever, ms


class AssistantTimeout(Exception):
    """The backend stopped WAITING for the pipeline. Python threads cannot be cancelled, so the call itself may still be
    running (and holding the pipeline lock) when this is raised; `still_running` says which. For a streamed call a stop
    is requested as well: the model stream ends at its next chunk (retrieval cannot be interrupted)."""

    def __init__(self, timeout_s: float, still_running: bool, stop_requested: bool = False):
        if not still_running:
            state = "the pipeline call has since finished; its result was discarded"
        elif stop_requested:
            state = ("the pipeline call is still running; a stop was requested and a streamed model response ends at its "
                     "next chunk; its result will be discarded")
        else:
            state = ("the pipeline call could not be cancelled and is still running in the background; its result will be "
                     "discarded")
        super().__init__(f"assistant did not answer within {timeout_s:g} s ({state})")
        self.still_running = still_running


def _streaming_refused(e: Exception) -> bool:
    """The provider rejected a streamed request outright (400/403 before any output), e.g. streaming not enabled for
    this account/model. The same request is then made without streaming."""
    try:
        import openai
    except ImportError:  # pragma: no cover
        return False
    return isinstance(e, (openai.BadRequestError, openai.PermissionDeniedError))


def make_budgeted_generator(attempt_timeout_s: float, max_retries: int, clock: StageClock | None = None,
                            client: Any = None, reasoning_effort: str | None = None):
    """pismo_assistant's OpenAIGenerator, unchanged except that its lazily created client gets an explicit per-attempt
    timeout and retry count (see Settings.llm_attempt_timeout_s), and that a call with a streaming observer (on `clock`)
    is streamed. The client still comes from the pipeline's own make_openai_client() (same key check and 'configuration'
    error); model, prompt (build_messages) and parsing (parse_output) are the pipeline's own. `reasoning_effort`
    (Settings.openai_reasoning_effort) is sent on streamed and non-streamed calls alike, and only when set."""
    from pismo_assistant.generation import (Generated, GenerationError, OpenAIGenerator, build_messages,
                                            make_openai_client, parse_output)

    class BudgetedOpenAIGenerator(OpenAIGenerator):
        @property
        def client(self):
            if self._client is None:
                self._client = make_openai_client().with_options(timeout=attempt_timeout_s, max_retries=max_retries)
            return self._client

        def generate(self, question, evidence):
            observer = getattr(clock, "observer", None)
            if observer is None:
                return super().generate(question, evidence)          # regular endpoint: the unchanged request
            return self._generate_streamed(question, evidence, observer)

        def _generate_streamed(self, question, evidence, observer: CallObserver):
            messages = build_messages(question, evidence)            # the same evidence-only prompt
            try:
                stream = self.client.chat.completions.create(model=self.model, messages=messages,
                                                             response_format={"type": "json_object"}, stream=True,
                                                             **self.request_options())
            except GenerationError:
                raise
            except Exception as e:
                if _streaming_refused(e):
                    return super().generate(question, evidence)
                raise GenerationError("api_error", f"{type(e).__name__}: {e}")
            deltas = AnswerDeltas()
            try:
                for chunk in stream:
                    if observer.stopped.is_set():
                        raise GenerationError("cancelled", "generation stopped because the request was abandoned")
                    choices = getattr(chunk, "choices", None) or []
                    piece = getattr(getattr(choices[0], "delta", None), "content", None) if choices else None
                    if piece:
                        text = deltas.feed(piece)
                        if text:
                            observer.emit("delta", {"text": text})
            except GenerationError:
                raise
            except Exception as e:  # connection dropped mid-stream, provider error event, ...
                raise GenerationError("api_error", f"{type(e).__name__}: {e}")
            finally:
                close = getattr(stream, "close", None)
                if close:
                    close()
            # the complete output, parsed exactly as the non-streamed path does (empty or partial JSON is rejected)
            status, answer, cites, missing = parse_output(deltas.raw)
            return Generated(status, answer, cites, missing, deltas.raw, self.model)

    return BudgetedOpenAIGenerator(client=client, reasoning_effort=reasoning_effort)


class Pipeline(Protocol):
    def answer(self, question: str) -> dict[str, Any]: ...


class AssistantService:
    def __init__(self, pipeline: Pipeline | None = None, timeout_s: float = 90.0, clock: StageClock | None = None,
                 llm_attempt_timeout_s: float = 40.0, llm_max_retries: int = 1, llm_reasoning_effort: str | None = None):
        self._pipeline = pipeline
        self._timeout_s = timeout_s
        self._clock = clock
        self._llm_budget = (llm_attempt_timeout_s, llm_max_retries)
        self.llm_reasoning_effort = llm_reasoning_effort
        self._load_lock = threading.Lock()
        self._call_lock = threading.Lock()
        self.load_error: str | None = None

    @property
    def loaded(self) -> bool:
        return self._pipeline is not None

    @property
    def index_version(self) -> str | None:
        """chunk_set_hash of the index held in memory, or None when nothing is loaded. Never triggers a load."""
        return _index_hash(self._pipeline)

    def _get(self) -> Pipeline:
        if self._pipeline is None:
            with self._load_lock:
                if self._pipeline is None:
                    try:
                        # the established AI engine, unchanged: same components Assistant() builds by default,
                        # passed through its constructor wrapped in timing proxies
                        from pismo_assistant.pipeline import Assistant
                        from pismo_assistant.retrieval import HybridRetriever
                        clock = StageClock()
                        generator = make_budgeted_generator(*self._llm_budget, clock=clock,
                                                            reasoning_effort=self.llm_reasoning_effort)
                        self._pipeline = Assistant(retriever=TimedRetriever(HybridRetriever(), clock),
                                                   generator=TimedGenerator(generator, clock))
                        self._clock = clock
                        self.load_error = None
                    except Exception as e:  # e.g. index integrity failure; message contains no secrets
                        self.load_error = f"{type(e).__name__}: {e}"[:300]
                        raise
        return self._pipeline

    def preload(self) -> None:
        self._get()

    def _call(self, question: str, done: threading.Event,
              observer: CallObserver | None = None) -> tuple[dict[str, Any], dict[str, Any], str | None]:
        try:
            t_start = time.perf_counter()
            pipeline = self._get()                  # waits for start-up preload / first load if still running
            t_loaded = time.perf_counter()
            if not self._call_lock.acquire(blocking=False):
                if observer is not None:
                    observer.emit("status", {"stage": "queued"})   # another request is using the pipeline
                self._call_lock.acquire()
            try:
                t_locked = time.perf_counter()
                if self._clock:
                    self._clock.reset(observer)
                result = pipeline.answer(question)
                t_done = time.perf_counter()
                timings: dict[str, Any] = {"load_wait_ms": ms(t_start, t_loaded), "lock_wait_ms": ms(t_loaded, t_locked),
                                           "pipeline_ms": ms(t_locked, t_done), "stages_measured": self._clock is not None}
                if self._clock:
                    timings.update(self._clock.stages(t_done))
                return result, timings, _index_hash(pipeline)   # the index of the pipeline that answered
            finally:
                self._call_lock.release()
        finally:
            done.set()

    async def answer_with_timings(self, question: str, observer: CallObserver | None = None
                                  ) -> tuple[dict[str, Any], dict[str, Any], str | None]:
        """(pipeline result, timings, chunk_set_hash of the index that served the call or None if unknown).
        With an observer (streaming endpoint) progress and provisional deltas are emitted, and abandoning the call
        (timeout or cancellation) asks a streamed model response to stop at its next chunk."""
        done = threading.Event()
        try:
            return await asyncio.wait_for(asyncio.to_thread(self._call, question, done, observer), timeout=self._timeout_s)
        except asyncio.TimeoutError as e:
            # only the wait is abandoned: the worker thread keeps running until the pipeline returns (bounded by the
            # LLM per-attempt timeout x attempts, or the next streamed chunk), keeps holding the pipeline lock, and its
            # result is discarded
            if observer is not None:
                observer.stop()
            raise AssistantTimeout(self._timeout_s, still_running=not done.is_set(),
                                   stop_requested=observer is not None) from e
        except asyncio.CancelledError:
            if observer is not None:                # client went away: stop a streamed model response early
                observer.stop()
            raise

    async def answer(self, question: str) -> dict[str, Any]:
        return (await self.answer_with_timings(question))[0]


def _index_hash(pipeline: Any) -> str | None:
    """chunk_set_hash computed once by HybridRetriever at load (reached through the timing proxy); None if absent."""
    h = getattr(getattr(pipeline, "retriever", None), "chunk_set_hash", None)
    return h if isinstance(h, str) and h else None


_service: AssistantService | None = None


def get_assistant_service() -> AssistantService:
    """FastAPI dependency (overridden in tests with a mocked pipeline)."""
    global _service
    if _service is None:
        from ..core.config import get_settings
        s = get_settings()
        _service = AssistantService(timeout_s=s.assistant_timeout_s, llm_attempt_timeout_s=s.llm_attempt_timeout_s,
                                    llm_max_retries=s.openai_max_retries, llm_reasoning_effort=s.openai_reasoning_effort)
    return _service
