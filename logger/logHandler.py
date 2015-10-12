
from common.Constants import Constants
#from common.monitorLog import monitorLog

# open file in init and close in destructor. Address Write Concurrency on log file. 
class LogHandler:

  def __init__ (self, service): 
    self.directory = "/" + Constants.LOGDIR + "/" + service
    self.filepath = directory + "/" + Constants.FILENAME
    if not os.path.exists(directory):
      try:
        os.makedirs(directory)
      except:
        #monitorLog.error()
    self.service = service
    self.setHost()
    self.setZone()
    self.setRegion()
    self.commonLog = Constants.toStringCommon(self.region, self.zone, self.host, self.service)  
    
  def appendLog (self, msg):
    try:
      fileHandler = open(self.filepath, "a")
      fileHandler.write(self.commonLog+msg)
      fileHandler.close()
      except IOError:
        pass
  
  '''
    Set host from metadata.
  '''
  def setHost(self):
    try:
      self.host = "demo_host"
    except:
      pass


  '''
    Set zone from metadata.
  '''    
  def setZone(self):
    try:
      self.host = "demo_zone"
    except:
      pass


  '''
    Set region from metadata.
  '''
  def setRegion(self):
    try:
      self.host = "demo_region"
    except:
      pass


