import unittest
import re
import os
from logger.logHandler import LogHandler
from logger.common.Constants import Constants
from test.demo_config import demoConfig

class TestLogHandler(unittest.TestCase):

  SERVICE = "demo_service"
  #socket = 5555

  def setUp(self):
    #TestLogHandler.socket = TestLogHandler.socket + 1
    #configWriter.CreateConfigFile("config.cfg", "Constants", "Socket", "tcp://127.0.0.1:"+`TestLogHandler.socket`)
    #configWriter.CreateConfigFile("config.cfg", "Constants", "LogDir", "./logs")
    #configWriter.CreateConfigFile("config.cfg", "Constants", "Filename", "metric.log")
    self.cfgfile = demoConfig().setConfig()

  def test_dirIfNotExists(self):
    logHandler = LogHandler(TestLogHandler.SERVICE, self.cfgfile)
    self.assertTrue(os.path.exists(os.path.join(os.path.join(Constants.getLogDir(), Constants.getHostname()),TestLogHandler.SERVICE)))

  def test_dirIfExists(self):
    new_logHandler = LogHandler(TestLogHandler.SERVICE, self.cfgfile)
    self.assertTrue(os.path.exists(os.path.join(os.path.join(Constants.getLogDir(), Constants.getHostname()),TestLogHandler.SERVICE)))

if __name__ == '__main__':
  unittest.main()

