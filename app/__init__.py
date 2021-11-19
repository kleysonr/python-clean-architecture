from typing import Any
from fastapi import FastAPI, Request


def create_app() -> FastAPI:

    # Create application
    app = FastAPI()

    @app.middleware("http")
    async def request_ctx_middleware(request: Request, call_next: Any) -> Any:
        response = await call_next(request)
        return response

    @app.on_event("startup")
    async def startup() -> None:
        pass

    @app.on_event("shutdown")
    async def shutdown() -> None:
        # cleanup
        pass

    return app
