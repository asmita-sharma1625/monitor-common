			
#Any common dependencies
import time
import threading

class Logger:
  


  '''
    It :
      - Create $LOGPATH/scopename/metric.log file if it does not exist
      - Initialize zone name, hostname and region which are common information for logging.
  '''
  def __init__ (self, service):
  	self.directory = "/"+scopename
	self.filepath = directory+"/"+Constants.FILENAME
	if not os.path.exists(directory):
    		os.makedirs(directory)
  	self.scope = scope
	self.zone = zone
	self.region = region
	self.threadLocal = threading.local()
  '''
    If the given action is failed, then it will log the failure
    It will return updated counter value.
  '''
  def LogIfFail (self, action, expectedreturn, metrictype, name):
  	

  '''
    Report the counter if the action is failed.
  '''
  def ReportCountEqual(self, action, expectedreturn, metrictype, name, counterval, value):
    pass
  
  
  def ReportCountNE(self, action, expectedreturn, metrictype, name, counterval, value):
    pass

  def StartTime (self):
	#using thread local storage for start time 
  	self.threadLocal.startTime = time.time()

  def ReportTime (self, metrictype, name):
 	 endTime = time.time()
	 runTime = endTime - self.threadLocal.startTime
	 fileHandler = open(self.filepath, "a")
	 fileHandler.write(Constants.toStringCommon(name, self.region, self.zone, self.scope, metrictype)+Constants.toStringRuntime(runTime))
	 


class Publish:
  def __init__(self, f):
      self.f = f

  def __call__(self, f):
    #Start
    self.f()
    #Stop
