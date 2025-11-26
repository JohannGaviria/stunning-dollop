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
    environment: str = Field(..., validation_alias="ENVIRONMENT")

    class Config:
        """Pydantic settings configuration."""

        env_file = ".env"


settings = Settings()  # type: ignore
