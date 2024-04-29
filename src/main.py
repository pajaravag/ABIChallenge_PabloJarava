import logging
import os

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from src.routes import health, index, inference

log = logging.getLogger("uvicorn")


def create_application() -> FastAPI:
    """Create FastAPI application
    Returns:
        FastAPI: FastAPI application
    """
    app = FastAPI()
    app.include_router(index.router)
    app.include_router(inference.router)
    app.include_router(health.router)
    return app


app = create_application()

register_tortoise(
    app,
    db_url=os.environ.get("DATABASE_URL"),
    modules={"models": ["src.models.database"]},
    generate_schemas=False,
    add_exception_handlers=True,
)


@app.on_event("startup")
async def startup_event():
    """Startup event."""
    log.info("Starting up...")


async def shutdown_event():
    """Shutdown event."""
    log.info("Shutting down...")
