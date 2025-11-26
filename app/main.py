"""This module contains the main FastAPI application."""

from fastapi import FastAPI

from app.config import settings

app = FastAPI(
    title=settings.app_name,
    summary=settings.app_summary,
    description=settings.app_description,
    version=settings.app_version,
    debug=settings.debug,
)


@app.get("/")
async def root():
    """Root endpoint providing basic application info."""
    return {
        "message": f"Welcome to {settings.app_name}!",
        "version": settings.app_version,
        "environment": settings.environment,
    }


@app.get("/ready")
async def ready():
    """Readiness check endpoint."""
    return {"ready": True}


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "OK"}
