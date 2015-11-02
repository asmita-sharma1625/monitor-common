import logging
import os
import socket
from common.Constants import Constants
from common.handler import Handler
from common.monitorLog import monitorLog

class LogHandler:

  def __init__ (self, service, configFile):
    self.service = service
    try:
      self.handler = Handler(self.service, configFile)
      self.logger = self.handler.getLogHandler()
    except Exception as error:
      monitorLog.logError("Cannot Instantiate Handler with configFile : " + configFile, error)
      raise Exception("Cannot Instantiate Handler with configFile : " + configFile)
    # start queue subscriber for logging 
    self.handler.startQueueSubscriber()
    # get queue handler for logging
    self.queueHandler = self.handler.getQueueHandler()
    self.commonLog = Constants.toStringCommon(service)

  def appendLog (self, msg):
    try:
      with self.queueHandler:
        self.logger.info(self.commonLog+msg)
    except Exception as error:
      monitorLog.logError("Failure to append Log: " + msg, error)
      raise Exception("Failure to append log: " + msg)

  def appendCountLog(self, name, metricType, count):
    msg = Constants.toStringCount(name, metricType, count)
    self.appendLog(msg)

  def appendTimeLog(self, name, metricType, runtime):
    msg = Constants.toStringRuntime(name, metricType, runtime)
    self.appendLog(msg)



