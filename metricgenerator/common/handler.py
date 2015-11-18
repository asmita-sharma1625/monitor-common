import os
import logging
from metricgenerator.common.Constants import Constants
from logbook.compat import RedirectLoggingHandler
from metricgenerator.common.zeroMQHandler import MyZeroMQHandler
from metricgenerator.common.configReader import ConfigReader
from metricgenerator.common.monitorLog import monitorLog
import zmq
''' not used since subscriber is an independent process now '''
'''
from metricgenerator.common.zeroMQSubscriber import MyZeroMQSubscriber
from multiprocessing import Process
import atexit
'''

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
    print "handler instantiated"

  def getLogHandler(self):
    print "returning logger instance :", `self.logger`
    return self.logger


  def getQueueHandler(self):
    print "returning queue handler"
    return MyZeroMQHandler(Constants.getSocket()).getZeroMQHandler()

  ''' Follwing methods are not used since subscriber is an independent process now '''
  '''
  def startQueueSubscriber(self):
    self.childProcess = Process(target = self.getQueueSubscriber)
    self.childProcess.daemon = True
    self.childProcess.start()
    #atexit.register(self.killQueueSubscriber)

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
  '''
