
#Any common dependencies
import time
import threading
from logHandler import LogHandler
from common.monitorLog import monitorLog
from common.exceptions import IncorrectConfigException, LoggingException
import traceback
class Logger:
  '''
  #beyond these, email will be triggered.
  threshold_failure = 20
  threshold_latency = 20
  threshold_count = 20
  '''
  '''
    It :
      - Creates LogHandler instance to write metrics to log file.
      - Creates threading.local() instance to create thread specific variables.
  '''
  def __init__ (self, service, configFile):
    try:
      print "logger instantiated"
      self.logHandler = LogHandler(service, configFile)
    except Exception as error:
      monitorLog.logError("Cannot Instantiate Logger with configFile : " + configFile, `error`)
      raise IncorrectConfigException("Cannot Instantiate Logger with configFile : " + configFile)
    self.threadLocal = threading.local()
    self.counter = 0;

  '''
    If the given action is failed, then it will log the failure count uptil now.
    It will also return the updated counter value.
  '''
  def logIfFail (self, name, expectedReturn, counter, action, severity = 20, *args, **kwargs):
    count = self.reportCountNE(expectedReturn, counter, action, *args, **kwargs)
    if count > 0:
      try:
        print "logging failure"
        self.logHandler.appendFailCountLog(name, count, severity)	
      except Exception as error:
        monitorLog.logError("Failed to append log for metric: " + name, `error`)
        raise LoggingException("Failed to append log for metric: " + name)
    return count

  def logFailure (self, name, counter, severity = 20):
    if counter > 0:
      try:
        '''
        if counter >= Logger.threshold_failure:
          self.logHandler.appendFailCountLog(name, counter,  50)
        '''
        self.logHandler.appendFailCountLog(name, counter, severity)
        print "logging failure"
      except Exception as error:
        monitorLog.logError("Failed to append log for metric: " + name, `error`)
        raise LoggingException("Failed to append log for metric: " + name)
      return 1
    return 0

  def logCount (self, name, counter, severity = 20):
    if counter > 0:
      try:
        print "inside logCount method for metric name - ", name
        '''
        if counter >= Logger.threshold_count:
          self.logHandler.appendCountLog(name, counter,  50)
        '''
        self.logHandler.appendCountLog(name, counter, severity)
      except Exception as error:
        monitorLog.logError("Failed to append log for metric: " + name, `error`)
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
  def reportTime (self, name, severity = 20):
    endTime = time.time()
    runTime = endTime - self.threadLocal.startTime
    try:
      '''
      if runTime >= Logger.threshold_latency:
        self.logHandler.appendTimeLog(name, runTime, 50)
      '''
      self.logHandler.appendTimeLog(name, runTime, severity)
    except Exception as error:
      monitorLog.logError("Failed to append log for metric: " + name, `error`)
      raise LoggingException("Failed to append log for metric: " + name+traceback.format_exc())

  '''
    Logs the execution time of the given action and returns the value of action.
  '''
  def reportLatency (self, name, action, severity = 20, *args, **kwargs):
    self.startTime()
    try:
      print "inside report Latency for metric name - ", name
      actualReturn = action(*args, **kwargs)
    except Exception as error:
      monitorLog.logError("Failed Action " + `action`, `error`)
      raise Exception("Failed Action :" + `action`)
    self.reportTime(name, severity)
    return actualReturn

