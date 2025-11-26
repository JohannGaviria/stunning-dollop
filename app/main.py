"""This module contains the main FastAPI application."""

import time

from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from starlette.responses import Response

from app.config import settings
from app.shared.cache.redis_client import RedisClient
from app.shared.db.database import Database

app = FastAPI(
    title=settings.app_name,
    summary=settings.app_summary,
    description=settings.app_description,
    version=settings.app_version,
    debug=settings.debug,
)


# Parse allowed origins for CORS from settings
allow_origins = [origin.strip() for origin in settings.cors_allow_origins.split(",")]

# Add CORS middleware to the application
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=settings.cors_allow_credentials,
    allow_methods=(
        [origin.strip() for origin in settings.cors_allow_methods.split(",")]
    ),
    allow_headers=(
        [origin.strip() for origin in settings.cors_allow_headers.split(",")]
    ),
)


# Métricas básicas
REQUEST_COUNT = Counter(
    "app_request_count",
    "Total number of requests",
    ["method", "endpoint", "http_status"],
)
REQUEST_LATENCY = Histogram(
    "app_request_latency_seconds", "Request latency", ["method", "endpoint"]
)


@app.middleware("http")
async def metrics_middleware(request, call_next):
    """Middleware to collect Prometheus metrics for each request.

    Args:
        request: The incoming HTTP request.
        call_next: The next middleware or endpoint handler.

    Returns:
        The HTTP response.
    """
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    REQUEST_LATENCY.labels(request.method, request.url.path).observe(process_time)
    REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()

    return response


@app.get("/metrics")
def metrics():
    """Endpoint to expose Prometheus metrics."""
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


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
    db = Database.health_check()
    redis = RedisClient.health_check()

    ready_status = db and redis

    return JSONResponse(
        content={
            "status": ready_status,
            "database": db,
            "redis": redis,
        },
        status_code=status.HTTP_200_OK,
    )


@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "OK"}
