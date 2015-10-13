return actualReturn
	 self.reportTime(name, metricType)
		pass
	 except:
		 actualReturn = action(*args, **kwargs)
	 try:
	 self.startTime()
  def reportLatency (self, name, metricType, action, *args, **kwargs):
  '''
    Logs the execution time of the given action.
  '''
	 self.logHandler.appendLog(logInfo)
	 logInfo = Constants.toStringRuntime(name, metricType, runTime)
	 runTime = endTime - self.threadLocal.startTime
 	 endTime = time.time()
  def reportTime (self, name, metricType):
  '''
    Stops the thread local timer and logs the execution time. 
  '''
  	self.threadLocal.startTime = time.time()
	#using thread local storage for start time 
  def startTime (self):
  '''
    Starts the thread local timer.
  '''

	return counter + 1
                 return
        if actualReturn == expectedReturn:
                 return counter + 1
        except:
                 actualReturn = action(*args, **kwargs)
	try:
  def reportCountNE(self, expectedReturn, counter, action, *args, **kwargs):
  '''  
    Report the incremented counter if the action has passed the expectation.
  '''

        return counter + 1
                 return
        if actualReturn == expectedReturn:
                 return counter + 1
        except:
                 actualReturn = action(*args, **kwargs)
        try:
  def reportCountEqual(self, expectedReturn, counter, action, *args, **kwargs):
  '''
    Report the incremented counter if the action has failed to pass the expectation.
  '''

		  	
	return count
		self.logHandler.appendLog(logInfo)	
		logInfo = Constants.toStringCount(name, metricType, count)
	if count > 0:
	count = self.ReportCountNE(expectedReturn, counter, action, *args, **kwargs)
  def logIfFail (self, name, metricType, expectedReturn, counter, action, *args, **kwargs):
  '''
    It will also return the updated counter value.
    If the given action is failed, then it will log the failure count uptil now.
  '''

	self.threadLocal = threading.local()
	# threading       #Stop
    self.f()
     #Stop
    self.f()
    #Start
  def __call__(self, f):

      self.f = f
  def __init__(self, f):
class Publish:


	 
	 fileHandler.write(Constants.toStringCommon(name, self.region, self.zone, self.scope, metrictype)+Constants.toStringRuntime(runTime))
	 fileHandler = open(self.filepath, "a")
	 runTime = endTime - self.threadLocal.startTime
 	 endTime = time.time()
  def ReportTime (self, metrictype, name):

  	self.threadLocal.startTime = time.time()
	#using thread local storage for start time 
  def StartTime (self):

    pass
  def ReportCountNE(self, action, expectedreturn, metrictype, name, counterval, value):
  
  
    pass
  def ReportCountEqual(self, action, expectedreturn, metrictype, name, counterval, value):
  '''
    Report the counter if the action is failed.
  '''

  	
  def LogIfFail (self, action, expectedreturn, metrictype, name):
  '''
    It will return updated counter value.
    If the given action is failed, then it will log the failure
  '''
	self.threadLocal = threading.local()
	self.region = region
	self.zone = zone
  	self.scope = scope
    		os.makedirs(directory)
	if not os.path.exists(directory):
	self.filepath = directory+"/"+Constants.FILENAME
  	self.directory = "/"+scopename
  def __init__ (self, service):
  '''
      - Initialize zone name, hostname and region which are common information for logging.
      - Create $LOGPATH/scopename/metric.log file if it does not exist
    It :
  '''


  
class Logger:

import threading
import time
#Any common dependencies

