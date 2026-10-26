"""Timeout/retry budget: every LLM attempt the SDK may make fits inside the backend deadline. No network: constructing
an OpenAI client does not contact the API, and the key used here is a placeholder."""
import os

import pytest

from backend.app.core.config import LLM_BUDGET_RESERVE_S, Settings
from backend.app.services import assistant_service
from backend.app.services.assistant_service import AssistantService, make_budgeted_generator

# pismo_assistant.config loads the project .env into os.environ on import; undo that (see test_timing.py).
_ENV_BEFORE = dict(os.environ)
from pismo_assistant.generation import GenerationError, OpenAIGenerator  # noqa: E402
os.environ.clear()
os.environ.update(_ENV_BEFORE)


def cfg(**kw):
    base = {"DATABASE_URL": "sqlite://", "ASSISTANT_TIMEOUT_S": 90, "OPENAI_TIMEOUT_S": 60, "OPENAI_MAX_RETRIES": 1}
    return Settings(_env_file=None, **{**base, **kw})


def test_default_budget_fits_the_deadline():
    s = cfg()
    assert s.openai_max_retries == 1 and s.llm_attempt_timeout_s == 40.0          # min(60, (90 - 10) / 2)
    assert (s.openai_max_retries + 1) * s.llm_attempt_timeout_s + LLM_BUDGET_RESERVE_S <= s.assistant_timeout_s


@pytest.mark.parametrize("deadline,ceiling,retries,expected", [
    (90, 60, 0, 60.0),      # no retry: the configured ceiling already fits
    (90, 30, 1, 30.0),      # a lower configured ceiling is respected
    (60, 60, 2, 16.7),      # (60 - 10) / 3
    (120, 60, 1, 55.0),     # (120 - 10) / 2
    (5, 60, 1, 1.0),        # absurdly small deadline: floor of 1 s rather than zero or negative
])
def test_attempt_timeout_is_derived_from_the_deadline(deadline, ceiling, retries, expected):
    s = cfg(ASSISTANT_TIMEOUT_S=deadline, OPENAI_TIMEOUT_S=ceiling, OPENAI_MAX_RETRIES=retries)
    assert s.llm_attempt_timeout_s == expected
    if deadline > LLM_BUDGET_RESERVE_S:
        assert (retries + 1) * s.llm_attempt_timeout_s + LLM_BUDGET_RESERVE_S <= deadline + 0.1


def test_retries_are_bounded():
    with pytest.raises(ValueError):
        cfg(OPENAI_MAX_RETRIES=4)


def test_generator_client_gets_the_budget(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "sk-placeholder-not-a-real-key")
    gen = make_budgeted_generator(40.0, 1)
    assert isinstance(gen, OpenAIGenerator) and gen.model          # same generator class and model setting as before
    client = gen.client
    assert client.timeout == 40.0 and client.max_retries == 1
    assert gen.client is client                                     # created once, lazily


def test_missing_key_still_reports_configuration_error(monkeypatch):
    monkeypatch.setenv("OPENAI_API_KEY", "")
    with pytest.raises(GenerationError) as e:
        make_budgeted_generator(40.0, 1).client
    assert e.value.kind == "configuration"


def test_service_is_built_from_settings(monkeypatch):
    s = cfg(ASSISTANT_TIMEOUT_S=70, OPENAI_MAX_RETRIES=2)
    monkeypatch.setattr(assistant_service, "_service", None)
    monkeypatch.setattr("backend.app.core.config.get_settings", lambda: s)
    svc = assistant_service.get_assistant_service()
    assert isinstance(svc, AssistantService)
    assert svc._timeout_s == 70 and svc._llm_budget == (s.llm_attempt_timeout_s, 2) == (20.0, 2)
