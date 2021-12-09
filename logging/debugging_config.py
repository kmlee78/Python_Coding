import logging
import logging.config
import sys

LOGGING_CONFIG = dict(
    version=1,
    loggers={
        "my_logger": {
            "level": "INFO",
            "handlers": ["console", "file_handler"],
            "propagte": "no",
        }
    },
    handlers={
        "console": {
            "class": "logging.StreamHandler",
            "level": "WARNING",
            "formatter": "simple",
            "stream": sys.stdout,
        },
        "file_handler": {
            "class": "logging.FileHandler",
            "level": "ERROR",
            "formatter": "simple",
            "filename": "info.log",
        },
    },
    formatters={
        "simple": {
            "class": "logging.Formatter",
            "format": "%(asctime)s  %(name)s  %(levelname)s  %(message)s",
        }
    },
)

logging.config.dictConfig(LOGGING_CONFIG)
logger = logging.getLogger("my_logger")

logger.info("this will be added to info.log")
logger.warning("this will be appeared on console as formatted")
logger.error("this will be appeared on console as formatted")
