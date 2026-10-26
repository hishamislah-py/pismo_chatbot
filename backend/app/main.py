"""FastAPI application. Run from the project root:

    python -m uvicorn backend.app.main:app --port 8000

OpenAPI docs: http://127.0.0.1:8000/docs. No authentication: local / access-controlled demo use only.
"""
import threading
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from .api import activity, health, messages, sessions
from .core.config import get_settings
from .services.assistant_service import get_assistant_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings = get_settings()
    if settings.assistant_preload:
        # load the index + embedding model in the background so the server starts immediately; /api/health shows progress
        threading.Thread(target=_safe_preload, daemon=True).start()
    yield


def _safe_preload():
    try:
        get_assistant_service().preload()
    except Exception:
        pass  # recorded in service.load_error and reported by /api/health


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title="Pismo Assistant API", version="0.1.0", lifespan=lifespan,
                  description="Conversation persistence around the existing Pismo AI pipeline. "
                              "No authentication: for local or access-controlled demo use only.")

    @app.middleware("http")
    async def limit_body_size(request: Request, call_next):
        length = request.headers.get("content-length")
        if length is not None and length.isdigit() and int(length) > settings.max_request_bytes:
            return JSONResponse(status_code=413, content={"detail": {"code": "request_too_large",
                                "message": f"request body exceeds {settings.max_request_bytes} bytes"}})
        return await call_next(request)

    app.add_middleware(CORSMiddleware, allow_origins=settings.cors_origin_list, allow_methods=["GET", "POST", "DELETE"],
                       allow_headers=["Content-Type"])
    for r in (health.router, sessions.router, messages.router, activity.router):
        app.include_router(r)
    return app


app = create_app()
