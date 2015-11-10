import os
import logging
from multiprocessing import Process
from logger.common.Constants import Constants
from logbook.compat import RedirectLoggingHandler
from logger.common.zeroMQHandler import MyZeroMQHandler
from logger.common.zeroMQSubscriber import MyZeroMQSubscriber
from logger.common.configReader import ConfigReader
import atexit
from logger.common.monitorLog import monitorLog
import zmq

class Handler:

  childProcess = None
 
  def __init__(self, service, configFile):
    ConfigReader.setConfig(configFile)
    try:
      self.directory = os.path.join(Constants.getLogDir(), os.path.join(Constants.getHostname(), service))
    except Exception, error:
      monitorLog.logError("Could not retrieve logging directory", error) 
      raise Exception("Could not retrieve logging directory")
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
      subscriber.startSubscriber(filepath)
    except zmq.error.ZMQError as error:
      monitorLog.logError("Subscriber process already running", error)
      pass
