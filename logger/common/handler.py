import os
import logging
from multiprocessing import Process
from logger.common.Constants import Constants
from logger.rotHandler import Rotator
from logbook.compat import RedirectLoggingHandler
from logger.common.zeroMQHandler import MyZeroMQHandler
from logger.common.zeroMQSubscriber import MyZeroMQSubscriber
import atexit

class Handler:

  childProcess = None
 
  def __init__(self, service, host):
    Constants.setLogDir(os.path.join(Constants.getLogDir(), host))
    try:
      #print os.getcwd()
      #pdb.set_trace()
      #print "GetLogDir "+Constants.getLogDir()
      self.directory = os.path.join(Constants.getLogDir(), service)
    except:
      print "log error message"
      return 
    if not os.path.exists(self.directory):
        os.makedirs(self.directory)
    #if not os.path.exists(self.filepath):
     # open(self.filepath, 'a').close() 
    self.logger = logging.getLogger(service)
    self.logger.setLevel(logging.INFO)
    self.logger.addHandler(RedirectLoggingHandler())
    #self.logger.addHandler(logging.FileHandler(self.filepath))
    #self.rotHandler = Rotator(self.filepath, 'M', 1, 10)
    #self.logger.addHandler(self.rotHandler)
    #self.host = host

  def getLogHandler(self):
    return self.logger


  def getQueueHandler(self):
    return MyZeroMQHandler(Constants.getSocket()).getZeroMQHandler()

  def startQueueSubscriber(self):
    #print "inside startQueueSubscriber"
    self.childProcess = Process(target = self.getQueueSubscriber)
    self.childProcess.start()
    atexit.register(self.killQueueSubscriber)
    #print "pid : " + `p.pid`

  def killQueueSubscriber(self):
    print "Kill Child process"
    self.childProcess.terminate()

  def getQueueSubscriber(self):
    #print "inside getQueueSubscriber with pid : " + `os.getpid()`
    filepath = os.path.join(self.directory, Constants.getFilename())
    subscriber = MyZeroMQSubscriber()
    subscriber.startSubscriber(filepath)
