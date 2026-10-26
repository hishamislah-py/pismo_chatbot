"""Per-stage timing of one pipeline call, measured at the two injection points pismo_assistant.pipeline.Assistant already
accepts (retriever, generator). pismo_assistant itself is not modified.

The wrappers only record monotonic start/end times around retriever.search() and generator.generate(); arguments,
return values and exceptions pass through unchanged, and every other attribute is forwarded to the wrapped object.
Assistant.answer() runs: retriever.search -> evidence assembly -> matched_operations -> generator.generate ->
citation validation / citation list. Stages between the two hooks are therefore measured as the gaps between them:

  retrieval_ms                 retriever.search (query embedding + hybrid search)
  evidence_and_operations_ms   search end -> generate start: evidence assembly, evidence serialisation and operation
                               matching (combined; they cannot be separated without changing pismo_assistant). When no
                               evidence is found, generate is not called and this runs to the end of answer().
  llm_ms                       generator.generate: prompt construction (<1 ms), OpenAI API wait, JSON parsing
  post_generation_ms           generate end -> answer() return: citation validation, citation list, warnings

Calls are serialised by AssistantService's lock, so one clock per service is safe; it is reset after the lock is taken.
All timings use time.perf_counter(): monotonic and high-resolution (time.monotonic() ticks in ~15.6 ms steps on Windows).

Progress (streaming endpoint only): the same hooks report stage boundaries to the call's observer, when one is attached
via reset(observer): "retrieving" when search starts, "evidence_ready" (with the evidence count) and "generating" when
generate starts, "validating" when generate has returned (citation validation follows). A stage is reported only when
it actually starts; without an observer nothing is emitted.
"""
import time
from typing import Any, Protocol


def ms(start: float, end: float) -> float:
    return round((end - start) * 1000, 1)


class Observer(Protocol):
    def emit(self, event: str, data: dict[str, Any]) -> None: ...


class StageClock:
    def __init__(self) -> None:
        self.search: tuple[float, float] | None = None
        self.generate: tuple[float, float] | None = None
        self.observer: Any = None          # the current call's progress observer (streaming), or None

    def reset(self, observer: Observer | None = None) -> None:
        self.search = self.generate = None
        self.observer = observer

    def emit(self, stage: str, **data: Any) -> None:
        if self.observer is not None:
            self.observer.emit("status", {"stage": stage, **data})

    def stages(self, end: float) -> dict[str, float | None]:
        s, g = self.search, self.generate
        return {
            "retrieval_ms": ms(*s) if s else None,
            "evidence_and_operations_ms": ms(s[1], g[0] if g else end) if s else None,
            "llm_ms": ms(*g) if g else None,
            "post_generation_ms": ms(g[1], end) if g else None,
        }


class _Timed:
    _method = ""

    def __init__(self, inner: Any, clock: StageClock) -> None:
        self._inner = inner
        self._clock = clock

    def __getattr__(self, name: str) -> Any:  # only called for attributes not defined here, e.g. retriever.chunks
        return getattr(self._inner, name)

    def _run(self, *args: Any, **kwargs: Any) -> Any:
        t0 = time.perf_counter()
        try:
            return getattr(self._inner, self._method)(*args, **kwargs)
        finally:
            setattr(self._clock, self._method, (t0, time.perf_counter()))


class TimedRetriever(_Timed):
    _method = "search"

    def search(self, *args: Any, **kwargs: Any) -> Any:
        self._clock.emit("retrieving")
        return self._run(*args, **kwargs)


class TimedGenerator(_Timed):
    _method = "generate"

    def generate(self, question: Any, evidence: Any, *args: Any, **kwargs: Any) -> Any:
        self._clock.emit("evidence_ready", evidence_count=len(evidence))
        self._clock.emit("generating")
        result = self._run(question, evidence, *args, **kwargs)
        self._clock.emit("validating")
        return result
