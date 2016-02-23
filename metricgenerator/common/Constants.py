import time
import socket
from configReader import ConfigReader
import configWriter
from monitorLog import monitorLog
import traceback

'''
		Declares constants.
'''
class Constants:

    #LOGDIR = ConfigReader.getValue("Constants", "LogDir")
    #FILENAME = ConfigReader.getValue("Constants", "Filename")
    #SOCKET = ConfigReader.getValue("Constants", "Socket")
    RUNTIME = "Runtime" #this will be measured in miliseconds
    FAILCOUNT = "Failure Count"
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

    def __init__(self, configFile):
        try:
            self.configReader = ConfigReader(configFile)
        except:
            monitorLog.logError("Cannot find config file : " + `configFile` + traceback.format_exc())
            self.logdir = "var/log/metricgenerator"
            self.filename = "metric.log"
            self.socket = "tcp://127.0.0.1:5522"
            pass

    def setLogDir(self, logdir):
        try:
            configWriter.CreateConfigFile("Constants", "LogDir", logdir)
        except:
            monitorLog.logError("Cannot update config file : " + `configFile` + traceback.format_exc())
            pass

    def getLogDir(self):
        try:
            self.logdir = self.configReader.getValue("Constants", "LogDir")
        except Exception:
            monitorLog.logError("Cannot get LogDir" + traceback.format_exc())
            pass
        return self.logdir

    def getFilename(self):
        try:
            self.filename = self.configReader.getValue("Constants", "Filename")
        except Exception:
            monitorLog.logError("Cannot get filename from config file" + traceback.format_exc())
            pass
        return self.filename

    def getSocket(self):
        try:
            self.socket = self.configReader.getValue("Constants", "Socket")
        except Exception:
            monitorLog.logError("Cannot get socket" + traceback.format_exc())
            pass
        return self.socket

    @staticmethod
    def getHostname():
        try:
            return socket.gethostname()
        except:
            monitorLog.logError("Cannot get hostname" + traceback.format_exc())
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
