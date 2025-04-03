from pydantic_settings import BaseSettings, SettingsConfigDict

from .version import __version__


class GlobalSettings(BaseSettings):
    model_config = SettingsConfigDict(
        # `.env.prod` takes priority over `.env`
        env_file=(".env", ".env.prod"),
        extra="ignore",
    )
    # defaults
    APP_VERSION: str = __version__
    ENVIRONMENT: str = "dev"
    LOG_LEVEL: str = "INFO"
    DEBUG: bool = False
    # required
    APP_NAME: str


settings = GlobalSettings()  # type: ignore[call-arg]


LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {
            "format": "%(asctime)s %(levelname)s [%(name)s:%(lineno)d] %(message)s",
            "datefmt": "%d-%m-%Y %I:%M:%S",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": settings.LOG_LEVEL,
            "formatter": "standard",
            "stream": "ext://sys.stdout",
        },
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": settings.LOG_LEVEL,
            "propagate": True,
        },
        "app": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "gunicorn.access": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
        "uvicorn.access": {
            "handlers": ["console"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}
