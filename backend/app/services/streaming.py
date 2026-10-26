"""Streaming support: a per-request observer that carries progress events from the pipeline's worker thread to the
event loop, and an incremental reader for the provisional answer text inside the model's JSON output.

Provisional text is only a preview. The model's complete output is parsed by pismo_assistant.generation.parse_output and
checked by the unchanged citation validation before anything is stored or sent as the final answer.
"""
import asyncio
import threading
from typing import Any

_ESCAPES = {'"': '"', "\\": "\\", "/": "/", "b": "\b", "f": "\f", "n": "\n", "r": "\r", "t": "\t"}


class CallObserver:
    """Thread-safe bridge for one request: emit() may be called from the worker thread; events land on an asyncio queue
    owned by the request's event loop. `stopped` tells a streaming model call to stop at its next chunk."""

    def __init__(self, loop: asyncio.AbstractEventLoop) -> None:
        self.loop = loop
        self.queue: asyncio.Queue = asyncio.Queue()
        self.stopped = threading.Event()

    def emit(self, event: str, data: dict[str, Any]) -> None:
        if self.stopped.is_set():
            return                                   # nobody is listening any more
        try:
            self.loop.call_soon_threadsafe(self.queue.put_nowait, (event, data))
        except RuntimeError:                         # loop already closed
            pass

    def stop(self) -> None:
        self.stopped.set()


def _read_string(raw: str, i: int) -> tuple[str, int, bool]:
    """Decode the JSON string starting at raw[i] == '"'. Returns (text so far, index after it, closed). Stops before an
    escape sequence that is not complete yet, so the returned prefix never changes once emitted."""
    out, j, n = [], i + 1, len(raw)
    while j < n:
        c = raw[j]
        if c == '"':
            return "".join(out), j + 1, True
        if c != "\\":
            out.append(c)
            j += 1
            continue
        if j + 1 >= n:
            break
        e = raw[j + 1]
        if e in _ESCAPES:
            out.append(_ESCAPES[e])
            j += 2
            continue
        if e != "u" or j + 6 > n:
            break                                    # incomplete \uXXXX (or invalid escape): wait for more
        try:
            cp = int(raw[j + 2:j + 6], 16)
        except ValueError:
            break
        if 0xD800 <= cp <= 0xDBFF:                   # high surrogate: needs the following \uXXXX low surrogate
            if j + 12 > n:
                break
            try:
                low = int(raw[j + 8:j + 12], 16) if raw[j + 6:j + 8] == "\\u" else -1
            except ValueError:
                break
            if 0xDC00 <= low <= 0xDFFF:
                out.append(chr(0x10000 + ((cp - 0xD800) << 10) + (low - 0xDC00)))
                j += 12
                continue
            break
        out.append(chr(cp))
        j += 6
    return "".join(out), j, False


def partial_answer(raw: str) -> str | None:
    """The (possibly incomplete) value of the TOP-LEVEL "answer" key in a JSON object that is still arriving, or None if
    it has not started. The word "answer" inside other strings or nested objects is ignored."""
    depth, i, n = 0, 0, len(raw)
    key: str | None = None
    expect_value = False
    while i < n:
        c = raw[i]
        if c == '"':
            text, end, closed = _read_string(raw, i)
            if depth == 1 and expect_value:
                if key == "answer":
                    return text
                expect_value = False
            elif depth == 1:
                key = text if closed else None
            if not closed:
                return None
            i = end
            continue
        if c in "{[":
            depth += 1
        elif c in "}]":
            depth -= 1
        elif depth == 1 and c == ":":
            expect_value = True
        elif depth == 1 and c == ",":
            expect_value, key = False, None
        i += 1
    return None


class AnswerDeltas:
    """Feed raw model output chunks; returns the newly visible provisional answer text after each one."""

    def __init__(self) -> None:
        self.raw = ""
        self.shown = ""

    def feed(self, chunk: str) -> str:
        self.raw += chunk
        text = partial_answer(self.raw)
        if text is None or len(text) <= len(self.shown) or not text.startswith(self.shown):
            return ""
        delta, self.shown = text[len(self.shown):], text
        return delta
