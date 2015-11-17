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
      monitorLog.logError("Cannot Instantiate Handler with configFile : " + configFile, `error`)
      raise Exception("Cannot Instantiate Handler with configFile : " + configFile)
    # start queue subscriber for logging 
    self.handler.startQueueSubscriber()
    # get queue handler for logging
    try:
      self.queueHandler = self.handler.getQueueHandler()
    except Exception as error:
      monitorLog.logError("Cannot instanstiate ZMQ handler with given context", `error`)
      raise Exception("Cannot instanstiate ZMQ handler with given context")
    self.commonLog = Constants.toStringCommon(service)

  '''
    Input - takes a string parameter 'msg' and an integer parameter specifying the logging level as 'severity'
    Logs the msg with the specified logging level.
  '''
  def appendLog (self, msg, severity):
    try:
      with self.queueHandler:
          self.logger.log(severity, self.commonLog+msg)
    except Exception as error:
      monitorLog.logError("Failure to append Log: " + msg, `error`)
      raise Exception("Failure to append log: " + msg)

  def appendFailCountLog(self, name, count, severity):
    msg = Constants.toStringCount(name, Constants.FAILCOUNT, count, severity)
    try:
      self.appendLog(msg, severity)
    except Exception as error:
      monitorLog.logError("Failure to append Count Log: " + msg, `error`)
      raise Exception("Failure to append Count log: " + msg)

  def appendCountLog(self, name, count, severity):
    msg = Constants.toStringCount(name, Constants.COUNT, count, severity)
    try:
      self.appendLog(msg, severity)
    except Exception as error:
      monitorLog.logError("Failure append Count Log: " + msg, `error`)
      raise Exception("Failure to append Count log: " + msg)

  def appendTimeLog(self, name, runtime, severity):
    msg = Constants.toStringRuntime(name, Constants.RUNTIME, runtime, severity)
    try:
      self.appendLog(msg, severity)
    except Exception as error:
      monitorLog.logError("Failure to append Count Log: " + msg, `error`)
      raise Exception("Failure to append Count log: " + msg)

  
