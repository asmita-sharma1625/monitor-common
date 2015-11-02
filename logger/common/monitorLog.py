# Initialize logger to log monitor events

import os
import sys
import logging
from logging import handlers
import pdb

class monitorLog:
  pdb.set_trace()
  logger = logging.getLogger("metric-generator")
  logger.setLevel(logging.INFO)
  directory = "/tmp/metric-generator/"
  if not os.path.exists(directory):
        os.makedirs(directory)
  #logger.addHandler(logging.FileHandler())
  logger.addHandler(logging.handlers.TimedRotatingFileHandler(os.path.join(directory, "metric.log"),'S', 2, 10))

  @staticmethod
  def logInfo(msg):
    monitorLog.logger.info(msg)

  @staticmethod
  def logError(msg, error):
    monitorLog.logger.error("Message: " + msg + "Error: " + `logging.exception(error)`)
