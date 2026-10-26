"""At most one message request in flight per session.

Why: a second message posted to the same session while the first is still generating would interleave the history
(question 1, question 2, answer 1, answer 2), would see question 1 as its follow-up context, and on PostgreSQL with
several workers could collide on the per-session sequence number only after the expensive pipeline call.

How the race is avoided: try_acquire() tests and marks the session inside one critical section of a threading.Lock, so
no other request (coroutine or thread) can pass the check between the test and the mark. The mark is removed in a
`finally`, so a pipeline error, a timeout or a cancelled request (client disconnect) always releases it.

Scope and limits: the guard is process-local and in memory. It is correct for the documented deployment (one uvicorn
process). With several worker processes or hosts it does NOT serialise requests across them; that would need a shared
lock (e.g. a PostgreSQL advisory lock), which is out of scope for this demo. Sessions are independent: holding one
session never blocks another (pipeline calls themselves are still serialised by AssistantService's lock).
"""
import threading
import uuid
from collections.abc import Iterator
from contextlib import contextmanager


class SessionBusy(Exception):
    def __init__(self, session_id: uuid.UUID):
        super().__init__(f"a message is already being processed for session {session_id}")
        self.session_id = session_id


class SessionGuard:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._busy: set[uuid.UUID] = set()

    def is_busy(self, session_id: uuid.UUID) -> bool:
        with self._lock:
            return session_id in self._busy

    @contextmanager
    def hold(self, session_id: uuid.UUID) -> Iterator[None]:
        """Mark the session busy for the duration of the block; raises SessionBusy if it already is."""
        with self._lock:                         # test-and-set: no gap between the check and the mark
            if session_id in self._busy:
                raise SessionBusy(session_id)
            self._busy.add(session_id)
        try:
            yield
        finally:                                 # also runs on timeout, error and cancellation
            with self._lock:
                self._busy.discard(session_id)


_guard = SessionGuard()


def get_session_guard() -> SessionGuard:
    """FastAPI dependency (tests may override it with a fresh guard)."""
    return _guard
