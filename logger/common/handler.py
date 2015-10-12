import os
import logging
from logger.common.Constants import Constants

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
    self.logger.addHandler(logging.FileHandler(self.filepath))

  def getLogHandler(self):
    return self.logger


