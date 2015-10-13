import logging
import os
from common.Constants import Constants
from common.monitorLog import monitorLog
from common.handler import Handler

# open file in init and close in destructor. Address Write Concurrency on log file. 
class LogHandler:

  def __init__ (self, service): 
    self.logger = Handler(service).getLogHandler()
    self.service = service
    self.setHost()
    self.setZone()
    self.setRegion()
    self.commonLog = Constants.setCommonString(self.region, self.zone, self.host, self.service)  
    
  def appendLog (self, msg):
    try:
      #fileHandler = open(self.filepath, "a")
      #fileHandler.write(self.commonLog+msg)
      #fileHandler.close()
      self.logger.info(self.commonLog+msg)
    except IOError:
      monitorLog.logError("Cannot write to file " + self.filepath) 
  
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


