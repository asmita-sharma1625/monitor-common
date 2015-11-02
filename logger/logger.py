
#Any common dependencies
import time
import threading
from logHandler import LogHandler
from common.monitorLog import monitorLog
from common.exceptions import IncorrectConfigException, LoggingException

class Logger:

  '''
    It :
      - Creates LogHandler instance to write metrics to log file.
      - Creates threading.local() instance to create thread specific variables.
  '''
  def __init__ (self, service, configFile):
    try:
      self.logHandler = LogHandler(service, configFile)
    except Exception as error:
      monitorLog.logError("Cannot Instantiate Logger with configFile : " + configFile, error)
      raise IncorrectConfigException("Cannot Instantiate Logger with configFile : " + configFile)
    self.threadLocal = threading.local()
    self.counter = 0;

  '''
    If the given action is failed, then it will log the failure count uptil now.
    It will also return the updated counter value.
  '''
  def logIfFail (self, name, metricType, expectedReturn, counter, action, *args, **kwargs):
    count = self.reportCountNE(expectedReturn, counter, action, *args, **kwargs)
    if count > 0:
      try:
        self.logHandler.appendCountLog(name, metricType, count)	
      except Exception as error:
        monitorLog.logError("Failed to append log for metric: " + name, error)
        raise LoggingException("Failed to append log for metric: " + name)
    return count

  def logFailure (self, name, metricType, counter):
    if counter > 0:
      try:
        self.logHandler.appendCountLog(name, metricType, counter)
      except Exception as error:
        monitorLog.logError("Failed to append log for metric: " + name, error)
        raise LoggingException("Failed to append log for metric: " + name)
      return 1
    return 0

  '''
    Report the incremented counter if the action has failed to pass the expectation.

  '''
  def reportCountEqual(self, expectedReturn, counter, action, *args, **kwargs):
    try:
      actualReturn = action(*args, **kwargs)
    except:
      return counter + 1
    if actualReturn == expectedReturn:
      return counter + 1
    return counter 

  '''
    Report the incremented counter if the action has passed the expectation.
  '''  
  def reportCountNE(self, expectedReturn, counter, action, *args, **kwargs):
    try:
      actualReturn = action(*args, **kwargs)
    except:
      return counter + 1
    if actualReturn == expectedReturn:
      return counter
    return counter + 1

  '''
    Starts the thread local timer.
  '''
  def startTime (self):
    #using thread local storage for start time 
    self.threadLocal.startTime = time.time()

  '''
    Stops the thread local timer and logs the execution time. 
  '''
  def reportTime (self, name, metricType):
    endTime = time.time()
    runTime = endTime - self.threadLocal.startTime
    try:
      self.logHandler.appendTimeLog(name, metricType, runTime)
    except Exception as error:
      monitorLog.logError("Failed to append log for metric: " + name, error)
      raise LoggingException("Failed to append log for metric: " + name)

  '''
    Logs the execution time of the given action and returns the value of action.
  '''
  def reportLatency (self, name, metricType, action, *args, **kwargs):
    self.startTime()
    try:
      actualReturn = action(*args, **kwargs)
    except Exception as error:
      monitorLog.logError("Failed : Action " + action, error)
      raise Exception("Failed :  Action :" + action)
    self.reportTime(name, metricType)
    return actualReturn

