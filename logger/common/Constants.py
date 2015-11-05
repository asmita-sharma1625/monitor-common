import time
import socket
from configReader import ConfigReader 
import configWriter
from monitorLog import monitorLog 

'''
	Declares constants.
'''
class Constants:

  #LOGDIR = ConfigReader.getValue("Constants", "LogDir")
  #FILENAME = ConfigReader.getValue("Constants", "Filename")
  #SOCKET = ConfigReader.getValue("Constants", "Socket")
  RUNTIME = "Runtime"
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
  

  @staticmethod
  def setLogDir(logdir):
    configWriter.updateConfigFile("Constants", "LogDir", logdir)

  @staticmethod
  def getLogDir():
    try:
      logdir = ConfigReader.getValue("Constants", "LogDir")
    except Exception as error:
      monitorLog.logError("Cannot get LogDir", error)
      raise error("Cannot get LogDir")
    return logdir

  @staticmethod
  def getFilename():
    try:
      filename = ConfigReader.getValue("Constants", "Filename")
    except Exception as error:
      monitorLog.logError("Cannot get filename", error)
      raise error("Cannot get filename")
    return filename

  @staticmethod
  def getSocket():
    try:
      socket = ConfigReader.getValue("Constants", "Socket")
    except Exception as error:
      monitorLog.logError("Cannot get socket", error)
      raise error("Cannot get socket")
    return socket

  '''
    Get host from metadata.
  '''
  @staticmethod
  def getHostname():
    try:
      hostname = socket.gethostname()
    except Exception as error:
      monitorLog.logError("Cannot get hostname", error)
      raise error("Cannot get hostname")
    return hostname  

  @staticmethod
  def toStringCommon (service):
    return Constants.HOST + Constants.SEPARATOR + Constants.getHostname() + Constants.DELIMITER + Constants.SERVICE + Constants.SEPARATOR + service + Constants.DELIMITER

  @staticmethod
  def appendTimestamp (string):
    return string + Constants.TIME + Constants.SEPARATOR + `time.time()` + Constants.DELIMITER

  @staticmethod
  def toStringRuntime (name, mType, runtime, severity):
    return Constants.appendSeverity ( Constants.appendTimestamp ( Constants.prependMetricInfo ( name, mType, Constants.METRIC_VALUE + Constants.SEPARATOR + `runtime` + Constants.DELIMITER ) ), severity )

  @staticmethod
  def toStringCount (name, mType, count, severity):
    return Constants.appendSeverity ( Constants.appendTimestamp ( Constants.prependMetricInfo ( name, mType, Constants.METRIC_VALUE + Constants.SEPARATOR + `count` + Constants.DELIMITER) ), severity )

  @staticmethod
  def prependMetricInfo(name, mType, string):
    return Constants.METRIC_NAME + Constants.SEPARATOR + name + Constants.DELIMITER + Constants.METRIC_TYPE + Constants.SEPARATOR + mType + Constants.DELIMITER + string

  @staticmethod
  def appendSeverity(string, severity):
    return string + Constants.SEVERITY + Constants.SEPARATOR + `severity` + Constants.DELIMITER 
