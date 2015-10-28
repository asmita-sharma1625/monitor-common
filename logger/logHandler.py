import logging
import os
import socket
from common.Constants import Constants
#from common.monitorLog import monitorLog
from common.handler import Handler
#from test import demoLogbookHandler

class LogHandler:

  def __init__ (self, service):
    self.service = service
    self.setHost()
    self.setZone()
    self.setRegion()
    self.handler = Handler(self.service, self.host)
    self.logger = self.handler.getLogHandler()
    # start queue subscriber for logging 
    self.handler.startQueueSubscriber()
    # get queue handler for logging
    self.queueHandler = self.handler.getQueueHandler()
    self.commonLog = Constants.toStringCommon(self.region, self.zone, self.host, self.service)

  def appendLog (self, msg):
    try:
      with self.queueHandler:
        self.logger.info(self.commonLog+msg)
    except:
      #monitorLog.logError("Cannot write to file " + self.filepath)
      pass

  def appendCountLog(self, name, metricType, count):
    msg = Constants.toStringCount(name, metricType, count)
    self.appendLog(msg)

  def appendTimeLog(self, name, metricType, runtime):
    msg = Constants.toStringRuntime(name, metricType, runtime)
    self.appendLog(msg)

  '''
    Set host from metadata.
  '''
  def setHost(self):
    try:
      self.host = socket.gethostname()
    except:
      pass


  '''
    Set zone from metadata.
  '''    
  def setZone(self):
    try:
      self.zone = "demo_zone"
    except:
      pass


  '''
    Set region from metadata.
  '''
  def setRegion(self):
    try:
      self.region = "demo_region"
    except:
      pass


