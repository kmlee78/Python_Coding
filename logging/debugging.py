import logging
from logging import Formatter, StreamHandler


def set_root_logger(level):
    logger = logging.getLogger()
    logger.setLevel(level=level)
    return logger


def set_custom_logger(name, propagate, *handlers):
    logger = logging.getLogger(name)
    for handler in handlers:
        logger.addHandler(handler)
    logger.propagate = propagate
    return logger


def level_test(logger):
    levels = [
        (logging.NOTSET, "NOTSET"),
        (logging.DEBUG, "DEBUG"),
        (logging.INFO, "INFO"),
        (logging.WARNING, "WARNING"),
        (logging.ERROR, "ERROR"),
        (logging.CRITICAL, "CRITICAL"),
    ]
    for level in levels:
        if logger.isEnabledFor(level=level[0]):
            print(f"logger has {level[1]} level")


def main():
    rootlogger = set_root_logger(level=logging.DEBUG)

    format_handler = StreamHandler()
    formatter = Formatter(
        "%(asctime)s  %(created)f  %(name)s  %(levelname)s  %(message)s"
    )
    format_handler.setFormatter(formatter)
    file_handler = logging.FileHandler("my.log")

    custumlogger = set_custom_logger("my_logger", True, format_handler, file_handler)

    level_test(custumlogger)
    custumlogger.debug("debug log printed")
    custumlogger.info("info log printed")
    custumlogger.warning("warning log printed")
    custumlogger.error("error log printed")
    custumlogger.critical("critical log printed")
    logging.error("log from root logger")


if __name__ == "__main__":
    main()
