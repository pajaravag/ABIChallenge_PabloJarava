import logging

from fastapi import FastAPI

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


@app.on_event("startup")
async def startup_event():
    """Startup event."""
    log.info("Starting up...")


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event."""
    log.info("Shutting down...")
