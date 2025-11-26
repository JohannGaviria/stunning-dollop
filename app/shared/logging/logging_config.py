"""This module contains the logging configuration."""

import logging
import sys

from pythonjsonlogger import json


class LoggingConfig:
    """Logging configuration class."""

    @staticmethod
    def configure(level: str, name: str) -> logging.Logger:
        """Configures the logging settings.

        Args:
            level (str): The logging level.
            name (str): The name of the logger.

        Returns:
            logger (logging.Logger): Configured logger instance.
        """
        logger = logging.getLogger(name=name)
        logger.setLevel(level=level)

        handler = logging.StreamHandler(stream=sys.stdout)
        formatter = json.JsonFormatter("%(asctime)s %(levelname)s %(name)s %(message)s")
        handler.setFormatter(fmt=formatter)

        if not logger.handlers:
            logger.addHandler(hdlr=handler)

        return logger
