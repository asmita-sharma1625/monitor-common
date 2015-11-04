import unittest
import re
import os
from logger.logHandler import LogHandler
from logger.common.Constants import Constants
from logger.common import configWriter
from logger.common.configReader import ConfigReader
#import pdb

class TestLogHandler(unittest.TestCase):

  SERVICE = "demo_service"
  socket = 6000

  def setUp(self):
    #pdb.set_trace()
    TestLogHandler.socket = TestLogHandler.socket + 1
    configWriter.CreateConfigFile("config.cfg", "Constants", "Socket", "tcp://127.0.0.1:"+`TestLogHandler.socket`)
    configWriter.CreateConfigFile("config.cfg", "Constants", "LogDir", ".")
    configWriter.CreateConfigFile("config.cfg", "Constants", "Filename", "metric.log")

  def test_dirIfNotExists(self):
   # pdb.set_trace()
    logHandler = LogHandler(TestLogHandler.SERVICE, "config.cfg")
    self.assertTrue(os.path.exists(os.path.join(os.path.join(Constants.getLogDir(), Constants.getHostname()),TestLogHandler.SERVICE)))

  def test_dirIfExists(self):
    new_logHandler = LogHandler(TestLogHandler.SERVICE, "config.cfg")
    self.assertTrue(os.path.exists(os.path.join(os.path.join(Constants.getLogDir(), Constants.getHostname()),TestLogHandler.SERVICE)))

if __name__ == '__main__':
  unittest.main()

