# Initialize logger to log monitor events

import os
import sys
import logging
from logging import handlers

class monitorLog:
    logger = logging.getLogger("metricgenerator")
    logger.setLevel(logging.INFO)
    directory = "/var/log/metricgenerator/metricgenerator"
    if not os.path.exists(directory):
                os.makedirs(directory)
    #logger.addHandler(logging.FileHandler())
    logger.addHandler(logging.handlers.TimedRotatingFileHandler(os.path.join(directory, "metric.log"),'S', 2, 10))

    @staticmethod
    def logInfo(msg):
        monitorLog.logger.info(msg)

    @staticmethod
    def logError(msg):
        monitorLog.logger.error(msg)
