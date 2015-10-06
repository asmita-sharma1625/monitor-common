
#Any common dependencies


class Logger:
  


  '''
    It :
      - Create $LOGPATH/scopename/metric.log file if it does not exist
      - Initialize zone name, hostname and region which are common information for logging.
  '''
  def __init__ (self, scopename, zonename, region):
    pass
  
  '''
    If the given action is failed, then it will log the failure
    It will return updated counter value.
  '''
  def LogIfFail (self, action, expectedreturn, metrictype, name):
    pass

  '''
    Report the counter if the action is failed.
  '''
  def ReportCountEqual(self, action, expectedreturn, metrictype, name, counterval, value):
    pass
  
  
  def ReportCountNE(self, action, expectedreturn, metrictype, name, counterval, value):
    pass

  def StartTime (self):
    pass

  def ReportTime (self, metrictype, name, val):
    pass



class Publish:
  def __init__(self, f):
      self.f = f

  def __call__(self, f):
    #Start
    self.f()
    #Stop
