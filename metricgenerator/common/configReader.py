import ConfigParser
import logging

log = logging.getLogger("metricgenerator")

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
            log.error("Cannot get LogDir", error)
            raise Exception("Cannot get LogDir")
        return value

