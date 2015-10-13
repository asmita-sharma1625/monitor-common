
#Any common dependencies
import time
import threading
import logHandler

class Logger:
  

  '''
    It :
      - Creates LogHandler instance to write metrics to log file.
      - Creates threading.local() instance to create thread specific variables.
  '''
  def __init__ (self, service):
  	self.logHandler = LogHandler(service)
	self.threadLocal = threading.local()


  '''
    If the given action is failed, then it will log the failure count uptil now.
    It will also return the updated counter value.
  '''
  def logIfFail (self, name, metricType, expectedReturn, counter, action, *args, **kwargs):
	count = self.ReportCountNE(expectedReturn, counter, action, *args, **kwargs)
	if count > 0:
		logInfo = Constants.toStringCount(name, metricType, count)
		self.logHandler.appendLog(logInfo)	
	return count
		  	

  '''
    Report the incremented counter if the action has failed to pass the expectation.
  '''
  def reportCountEqual(self, expectedReturn, counter, action, *args, **kwargs):
        try:
                 actualReturn = action(*args, **kwargs)
        except:
                 return counter + 1
        if actualReturn == expectedReturn:
                 return
        return counter + 1

  '''
    Report the incremented counter if the action has passed the expectation.
  '''  
  def reportCountNE(self, expectedReturn, counter, action, *args, **kwargs):
	try:
                 actualReturn = action(*args, **kwargs)
        except:
                 return counter + 1
        if actualReturn == expectedReturn:
                 return
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
	 logInfo = Constants.toStringRuntime(name, metricType, runTime)
	 self.logHandler.appendLog(logInfo)
  '''
    Logs the execution time of the given action and returns the value of action.
  '''
  def reportLatency (self, name, metricType, action, *args, **kwargs):
	 self.startTime()
	 try:
		 actualReturn = action(*args, **kwargs)
	 except:
		pass
	 self.reportTime(name, metricType)
	 return actualReturn
