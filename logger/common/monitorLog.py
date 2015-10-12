# Initialize logger to log monitor events

from logger.common.handler import Handler

class monitorLog:
  
  logger = Handler("monitor").getLogHandler()

  def logInfo(self, msg):
    logger.info(msg)

  def logError(self, msg):
    logger.error(msg)
