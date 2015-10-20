import os
import logging
from multiprocessing import Process
from logger.common.Constants import Constants
from logger.rotHandler import Rotator
from logbook.compat import RedirectLoggingHandler
from logger.common.zeroMQHandler import MyZeroMQHandler
from logger.common.zeroMQSubscriber import MyZeroMQSubscriber
class Handler:
  
  def __init__(self, service):
    self.directory = os.path.join(Constants.LOGDIR, service)
    self.filepath = os.path.join(self.directory, Constants.FILENAME)
    if not os.path.exists(self.directory):
        os.makedirs(self.directory)
    if not os.path.exists(self.filepath):
      open(self.filepath, 'a').close() 
    self.logger = logging.getLogger(service)
    self.logger.setLevel(logging.INFO)
    self.logger.addHandler(RedirectLoggingHandler())
#    self.logger.addHandler(logging.FileHandler(self.filepath))
    #self.rotHandler = Rotator(self.filepath, 'M', 1, 10)
    #self.logger.addHandler(self.rotHandler)

  def getLogHandler(self):
    return self.logger


  def getQueueHandler(self):
    return MyZeroMQHandler(Constants.SOCKET).getZeroMQHandler()

  def startQueueSubscriber(self):
    subscriber = MyZeroMQSubscriber(Constants.SOCKET)
    p = Process(target=subscriber.startSubscriber, args =())
    p.start()
    p.join()

