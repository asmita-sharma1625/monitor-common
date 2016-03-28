import time
import socket
import os
from configReader import ConfigReader
import configWriter
import logging
import monitorLog
import traceback

log = logging.getLogger("metricgenerator")

'''
		Declares constants.
'''
class Constants:

    #LOGDIR = ConfigReader.getValue("Constants", "LogDir")
    #FILENAME = ConfigReader.getValue("Constants", "Filename")
    #SOCKET = ConfigReader.getValue("Constants", "Socket")
    RUNTIME = "Runtime" #this will be measured in miliseconds
    FAILCOUNT = "Failure"
    COUNT = "Counter"
# Use constants for metric type
    METRIC_TYPE = "Metric Type"
    METRIC_NAME = "Metric Name"
    HOST = "Host"
    SERVICE = "Service"
    TIME = "Timestamp"
    SEVERITY = "Severity"
    METRIC_VALUE = "Metric Value"
    SEPARATOR = " : "
    DELIMITER = "\n"
    logdir = "/var/log/metricgenerator"
    filename = "metric.log"
    mylogpath = "/tmp/metricgenerator.log"
    socket = "tcp://127.0.0.1:5522"
    mylogformat = "%(asctime)s - %(name)s - %(pathname)s - %(funcName)s -%(thread)d - %(levelname)s - %(message)s"

    def __init__(self, configFile):
        try:
            self.configReader = ConfigReader(configFile)
        except:
            print "ERROR: Unable to find config file : " + `configFile`
            raise Exception("ERROR: Unable to find config file : " + `configFile`)
        finally:
            try:
                monitorLog.configure_logging(self.getMyLogFormat(), self.getMyLogPath())
            except:
                print "ERROR : Unable to configure logging.", traceback.format_exc()
                raise Exception("ERROR : Unable to configure logging.")

    def getLogDir(self):
        try:
            logdir = self.configReader.getValue("Constants", "LogDir")
        except Exception:
            log.error("Cannot get LogDir")
            logdir = Constants.logdir
            pass
        return logdir

    def getFilename(self):
        try:
            filename = self.configReader.getValue("Constants", "filename")
        except Exception:
            log.error("Cannot get filename from config")
            filename = Constants.filename
            pass
        return filename


    def getMyLogFormat(self):
        try:
            mylogformat = self.configReader.getValue("Constants", "MyLogFormat")
        except Exception:
            log.error("Cannot get my log format")
            mylogformat = Constants.mylogformat
            pass
        return mylogformat

    def getMyLogPath(self):
        try:
            mylogdir = self.configReader.getValue("Constants", "MyLogDir")
            mylogfile = self.configReader.getValue("Constants", "MyLogFile")
            mylogpath = os.path.join(mylogdir, mylogfile)
        except:
            log.error("Cannot get my log path")
            mylogpath = Constants.mylogpath
            pass
        return mylogpath

    def getSocket(self):
        try:
            socket = self.configReader.getValue("Constants", "Socket")
        except Exception:
            log.error("Cannot get socket")
            socket = Constants.socket
            pass
        return socket

    @staticmethod
    def getHostname():
        try:
            return socket.gethostname()
        except:
            log.error("Cannot get hostname")
            return None

    @staticmethod
    def createDictCommon (service):
        commonDict = {
            Constants.HOST : Constants.getHostname(),
            Constants.SERVICE : service
        }
        return commonDict

    @staticmethod
    def addTimeStamp (customDict):
        customDict.update({Constants.TIME : time.time()})
        return customDict

    @staticmethod
    def toDictRuntime (name, mType, runtime, severity):
        customDict = { Constants.METRIC_VALUE : runtime }
        return Constants.addSeveriety ( Constants.addTimeStamp (
            Constants.addMetricInfo ( name, mType, customDict ) ), severity)

    @staticmethod
    def toDictCount (name, mType, count, severity):
        customDict = { Constants.METRIC_VALUE : count }
        return Constants.addSeveriety ( Constants.addTimeStamp (
            Constants.addMetricInfo ( name, mType, customDict ) ), severity)


    @staticmethod
    def addMetricInfo (name, mType, customDict):
        metricDict = {
            Constants.METRIC_NAME : name,
            Constants.METRIC_TYPE : mType
        }
        customDict.update(metricDict)
        return customDict

    @staticmethod
    def addSeveriety (customDict, severity):
        severityDict = {Constants.SEVERITY : severity}
        customDict.update(severityDict)
        return customDict

    @staticmethod
    def addKeyValue (key, value, customDict = {}):
        pair = {key : value}
        customDict.update(pair)
        return customDict
