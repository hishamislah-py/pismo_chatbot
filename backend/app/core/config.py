"""Environment-based settings. Values come from the process environment, then the project-root .env file.
Secrets (OPENAI_API_KEY, database password) are never logged or returned by the API."""
from functools import lru_cache
from pathlib import Path

from urllib.parse import quote

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

PROJECT_ROOT = Path(__file__).resolve().parents[3]
LLM_BUDGET_RESERVE_S = 10.0   # part of ASSISTANT_TIMEOUT_S kept for retrieval, retry back-off and persistence
# OPENAI_REASONING_EFFORT values allowed for the answer call: values of the installed SDK's ReasoningEffort type that are
# confirmed with gpt-5-mini in this project ("minimal": router classifier; "low": answer experiment 2026-10-22). Other
# SDK values (medium, high, ...) are not accepted until verified with the configured model.
ANSWER_REASONING_EFFORTS = ("minimal", "low")


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=str(PROJECT_ROOT / ".env"), env_file_encoding="utf-8", extra="ignore")

    database_url: str | None = Field(default=None, alias="DATABASE_URL")
    # Docker Compose database (docker-compose.yml). Used to build DATABASE_URL when it is not set explicitly.
    pismo_db_app_password: str | None = Field(default=None, alias="PISMO_DB_APP_PASSWORD", repr=False)
    pismo_db_host_port: int = Field(default=5434, alias="PISMO_DB_HOST_PORT", ge=1, le=65535)
    # IPv4 loopback, not "localhost": the container is published on 127.0.0.1 only, and on this Windows host "localhost"
    # tries ::1 first, which stalls ~10 s per new connection before falling back to IPv4.
    pismo_db_host: str = Field(default="127.0.0.1", alias="PISMO_DB_HOST", min_length=1)
    # Assistant pipeline. Timeout budget for one message (see llm_attempt_timeout_s):
    #   ASSISTANT_TIMEOUT_S  backend deadline for the whole pipeline call (load wait + lock wait + retrieval + LLM + checks)
    #   OPENAI_MAX_RETRIES   SDK retries after a failed LLM attempt (connection error, timeout, 408/409/429/5xx)
    #   OPENAI_TIMEOUT_S     upper bound for ONE LLM attempt; lowered automatically so that all attempts fit the deadline
    assistant_timeout_s: float = Field(default=90.0, alias="ASSISTANT_TIMEOUT_S", gt=0)
    openai_timeout_s: float = Field(default=60.0, alias="OPENAI_TIMEOUT_S", gt=0)
    openai_max_retries: int = Field(default=1, alias="OPENAI_MAX_RETRIES", ge=0, le=3)
    # Answer-generation reasoning effort (not the router's: see ROUTER_REASONING_EFFORT). Unset or empty = the parameter
    # is not sent, which is the behaviour before this setting existed (the model's own default).
    openai_reasoning_effort: str | None = Field(default=None, alias="OPENAI_REASONING_EFFORT")
    assistant_preload: bool = Field(default=True, alias="ASSISTANT_PRELOAD")
    # First-stage routing classifier (services/router.py): one call, no retries, before any retrieval. Its timeout is
    # spent before the pipeline deadline: ROUTER_TIMEOUT_S + ASSISTANT_TIMEOUT_S (8 + 90 by default) stays below the
    # frontend's 120 s. ROUTER_MODEL defaults to the configured answer model (OPENAI_MODEL), which the account is known
    # to have access to; a smaller model can be set once verified. ROUTER_REASONING_EFFORT applies to reasoning models.
    router_enabled: bool = Field(default=True, alias="ROUTER_ENABLED")
    router_model: str | None = Field(default=None, alias="ROUTER_MODEL")
    openai_model: str = Field(default="gpt-5-mini", alias="OPENAI_MODEL")
    router_timeout_s: float = Field(default=8.0, alias="ROUTER_TIMEOUT_S", gt=0, le=30)
    router_reasoning_effort: str | None = Field(default="minimal", alias="ROUTER_REASONING_EFFORT")
    # Session-scoped follow-up context (prior USER questions of the same session only)
    context_max_prior_questions: int = Field(default=2, alias="CONTEXT_MAX_PRIOR_QUESTIONS", ge=0, le=10)
    context_max_chars: int = Field(default=600, alias="CONTEXT_MAX_CHARS", ge=0, le=4000)
    # Request limits
    max_question_chars: int = Field(default=2000, alias="MAX_QUESTION_CHARS", ge=1)
    max_request_bytes: int = Field(default=16384, alias="MAX_REQUEST_BYTES", ge=1024)
    # Local React dev servers (Vite / CRA). Comma-separated.
    cors_origins: str = Field(default="http://localhost:5173,http://localhost:3000", alias="CORS_ORIGINS")

    @field_validator("openai_reasoning_effort", mode="before")
    @classmethod
    def _check_reasoning_effort(cls, v):
        v = (v or "").strip().lower() if isinstance(v, str) or v is None else v
        if not v:
            return None
        if v not in ANSWER_REASONING_EFFORTS:
            raise ValueError(f"OPENAI_REASONING_EFFORT must be one of {', '.join(ANSWER_REASONING_EFFORTS)} "
                             f"or empty (model default); got {v!r}")
        return v

    @model_validator(mode="after")
    def _derive_database_url(self):
        if not (self.database_url or "").strip():
            self.database_url = None
            if self.pismo_db_app_password:
                pw = quote(self.pismo_db_app_password, safe="")
                self.database_url = f"postgresql+psycopg://pismo_app:{pw}@{self.pismo_db_host}:{self.pismo_db_host_port}/pismo_assistant"
        return self

    @property
    def llm_attempt_timeout_s(self) -> float:
        """Per-attempt OpenAI timeout: OPENAI_TIMEOUT_S, lowered so (retries + 1) attempts plus LLM_BUDGET_RESERVE_S
        (retrieval, normal retry back-off, persistence) fit inside ASSISTANT_TIMEOUT_S. Defaults: min(60, (90-10)/2) = 40 s.
        A server Retry-After longer than the reserve is honoured by the SDK and can still exceed the deadline; the
        backend then answers 504 honestly while the call finishes in the background."""
        share = (self.assistant_timeout_s - LLM_BUDGET_RESERVE_S) / (self.openai_max_retries + 1)
        return round(max(1.0, min(self.openai_timeout_s, share)), 1)

    @property
    def router_model_name(self) -> str:
        return (self.router_model or "").strip() or self.openai_model

    @property
    def cors_origin_list(self) -> list[str]:
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
