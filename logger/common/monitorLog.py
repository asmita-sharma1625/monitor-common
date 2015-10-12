# Initialize logger to log monitor events

import logging
import Constants

class monitorLog:
  logger = logging.getLogger('monitor_app')
  fileHandle = logging.FileHandler(Constants.LOGDIR+"/monitor/"+Constants.FILENAME)

  def logInfo(self, msg):
    logger.info(msg)

  def logError(self, msg):
    logger.error(msg)
