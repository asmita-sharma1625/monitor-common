import logging
import os
import socket
from common.Constants import Constants
from common.handler import Handler
from common.monitorLog import monitorLog
import threading

class LogHandler:

  def __init__ (self, service, configFile):
    self.service = service
    try:
      self.handler = Handler(self.service, configFile)
      self.logger = self.handler.getLogHandler()
      print "handler returned logger instance"
    except Exception as error:
      monitorLog.logError("Cannot Instantiate Handler with configFile : " + configFile, `error`)
      raise Exception("Cannot Instantiate Handler with configFile : " + configFile)
    ''' Subscriber is now an independent process , hence following lines are commented '''
    # start queue subscriber for logging 
    # self.handler.startQueueSubscriber()
    # get queue handler for logging
    try:
      self.queueHandler = self.handler.getQueueHandler()
    except Exception as error:
      monitorLog.logError("Cannot instanstiate ZMQ handler with given context", `error`)
      raise Exception("Cannot instanstiate ZMQ handler with given context")
    self.commonLog = Constants.toStringCommon(service)
    #self.mutex = threading.Lock()

  '''
    Input - takes a string parameter 'msg' and an integer parameter specifying the logging level as 'severity'
    Logs the msg with the specified logging level.
  '''
  def appendLog (self, msg, severity):
    try:
      with self.queueHandler:
          mutex = threading.Lock() #self.mutex
          #print "@inside appendLog - acquiring lock- ", msg
          mutex.acquire(True)
          print "@acquiring lock- "
          self.logger.log(severity, self.commonLog+msg)
          print "@releasing lock"
          mutex.release()
          print "@Lock released"
          print "appended log"
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

  
