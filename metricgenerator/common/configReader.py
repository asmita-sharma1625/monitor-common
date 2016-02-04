import ConfigParser
#import configWriter
from monitorLog import monitorLog

class ConfigReader:
    config = ConfigParser.RawConfigParser()

    def __init__(self, configFile):
        #print "Config file is "+configFile
        self.config.read(configFile)
        #configWriter.setConfigFile(configFile)
        #print "Config Read Done "+ConfigReader.getValue("Constants","LogDir")

    def getValue(self, section, key):
        try:
            value = self.config.get(section, key)
        except ConfigParser.NoSectionError as error:
            monitorLog.logError("Cannot get LogDir", error)
            raise Exception("Cannot get LogDir")
        return value

