import logging
import os
from common.Constants import Constants
from common.monitorLog import monitorLog
from common.handler import Handler
from test import demoLogbookHandler
#from test import demoMultiProcessingHandler

# open file in init and close in destructor. Address Write Concurrency on log file. 
class LogHandler:

  def __init__ (self, service):
    self.logger = Handler(service).getLogHandler()
    self.service = service
    self.setHost()
    self.setZone()
    self.setRegion()
    self.commonLog = Constants.toStringCommon(self.region, self.zone, self.host, self.service)

  def appendLog (self, msg):
    try:
      with demoLogbookHandler.handler:
        self.logger.info(self.commonLog+msg)
    except IOError:
      monitorLog.logError("Cannot write to file " + self.filepath)

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
      self.host = "demo_host"
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


