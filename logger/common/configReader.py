import ConfigParser

class ConfigReader:  
  
  config = ConfigParser.RawConfigParser()

  @staticmethod
  def setConfig(configFile):
    print "Config file is "+configFile
    ConfigReader.config.read(configFile)
    print "Config Read Done "+ConfigReader.getValue("Constants","LogDir")
  
  @staticmethod
  def getValue(section, key):
    return ConfigReader.config.get(section, key)

