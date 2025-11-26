"""This module contains the application configuration settings using Pydantic."""

from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application configuration settings."""

    # Application metadata
    app_name: str = Field(..., validation_alias="APP_NAME")
    app_summary: str = Field(..., validation_alias="APP_SUMMARY")
    app_description: str = Field(..., validation_alias="APP_DESCRIPTION")
    app_version: str = Field(..., validation_alias="APP_VERSION")
    debug: bool = Field(False, validation_alias="DEBUG")

    # Backend configuration
    backed_port: int = Field(..., validation_alias="BACKEND_PORT")
    backend_host: str = Field(..., validation_alias="BACKEND_HOST")
    backend_workers: int = Field(..., validation_alias="BACKEND_WORKERS")
    acme_email: str = Field(..., validation_alias="ACME_EMAIL")
    traefik_auth: str = Field(..., validation_alias="TRAEFIK_AUTH")
    gf_security_admin_password: str = Field(
        ..., validation_alias="GF_SECURITY_ADMIN_PASSWORD"
    )
    environment: str = Field(..., validation_alias="ENVIRONMENT")

    # Database configuration
    database_url: str = Field(..., validation_alias="DATABASE_URL")
    db_port: int = Field(..., validation_alias="DB_PORT")
    postgres_user: str = Field(..., validation_alias="POSTGRES_USER")
    postgres_db: str = Field(..., validation_alias="POSTGRES_DB")
    postgres_password: str = Field(..., validation_alias="POSTGRES_PASSWORD")

    # Redis configuration
    redis_port: int = Field(..., validation_alias="REDIS_PORT")
    redis_password: str = Field(..., validation_alias="REDIS_PASSWORD")
    redis_host: str = Field(..., validation_alias="REDIS_HOST")
    redis_db: int = Field(..., validation_alias="REDIS_DB")

    # CORS
    cors_allow_origins: str = Field(..., validation_alias="CORS_ALLOW_ORIGINS")
    cors_allow_credentials: bool = Field(..., validation_alias="CORS_ALLOW_CREDENTIALS")
    cors_allow_methods: str = Field(..., validation_alias="CORS_ALLOW_METHODS")
    cors_allow_headers: str = Field(..., validation_alias="CORS_ALLOW_HEADERS")

    class Config:
        """Pydantic settings configuration."""

        env_file = ".env"


settings = Settings()  # type: ignore
