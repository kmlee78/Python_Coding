# https://hamait.tistory.com/880
import logging
import logging.config
import json

with open("logging.json", "rt") as f:
    config = json.load(f)

    logging.config.dictConfig(config)

    logger = logging.getLogger("my_logger")
    logger.info("this will be added to info.log")
    logger.warning("this will be appeared on console as formatted")
    logger.error("this will be appeared on console as formatted")
