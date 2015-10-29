import os
import logging
from multiprocessing import Process
from logger.common.Constants import Constants
from logbook.compat import RedirectLoggingHandler
from logger.common.zeroMQHandler import MyZeroMQHandler
from logger.common.zeroMQSubscriber import MyZeroMQSubscriber
from logger.common.configReader import ConfigReader
import atexit

class Handler:

  childProcess = None
 
  def __init__(self, service, configFile):
    ConfigReader.setConfig(configFile)
    try:
      self.directory = os.path.join(Constants.getLogDir(), os.path.join(Constants.getHostname(), service))
    except:
      print "log error message"
      return 
    if not os.path.exists(self.directory):
        os.makedirs(self.directory)
    self.logger = logging.getLogger(service)
    self.logger.setLevel(logging.INFO)
    self.logger.addHandler(RedirectLoggingHandler())

  def getLogHandler(self):
    return self.logger


  def getQueueHandler(self):
    return MyZeroMQHandler(Constants.getSocket()).getZeroMQHandler()

  def startQueueSubscriber(self):
    self.childProcess = Process(target = self.getQueueSubscriber)
    self.childProcess.start()
    atexit.register(self.killQueueSubscriber)

  def killQueueSubscriber(self):
    print "Kill Child process"
    self.childProcess.terminate()

  def getQueueSubscriber(self):
    filepath = os.path.join(self.directory, Constants.getFilename())
    try:
      subscriber = MyZeroMQSubscriber()
    except ZMQError:
      pass
    subscriber.startSubscriber(filepath)
