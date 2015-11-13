import ConfigParser
#import configWriter 
from monitorLog import monitorLog

class ConfigReader:  
  
  config = ConfigParser.RawConfigParser()

  @staticmethod
  def setConfig(configFile):
    #print "Config file is "+configFile
    ConfigReader.config.read(configFile)
    #configWriter.setConfigFile(configFile)
    #print "Config Read Done "+ConfigReader.getValue("Constants","LogDir")
  
  @staticmethod
  def getValue(section, key):
    try:
      value = ConfigReader.config.get(section, key)
    except ConfigParser.NoSectionError as error:
      monitorLog.logError("Cannot get LogDir", error)
      raise Exception("Cannot get LogDir")
    return value

