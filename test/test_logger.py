import unittest
from logger import logger
from logger.common import configWriter
from logger.common.configReader import ConfigReader

class TestLogger(unittest.TestCase):
  
  SERVICE = "TestLogger"
  NAME = "dummy_metric"
  MTYPE = "debug"
  socket = 5000

  def setUp(self):
    TestLogger.socket = TestLogger.socket + 1
    configWriter.CreateConfigFile("Config.cfg", "Constants", "Socket", "tcp://127.0.0.1:"+`TestLogger.socket`)
    configWriter.CreateConfigFile("Config.cfg", "Constants", "LogDir", ".")
    configWriter.CreateConfigFile("Config.cfg", "Constants", "Filename", "metric.log")
    self.logger = logger.Logger(self.SERVICE, "Config.cfg")

  def dummy_func(self, a, b):
    return a / b  

  def test_logFailure_fail(self):
    self.assertEquals(self.logger.logFailure(self.NAME, self.MTYPE, 0), 0)

  def test_logFailure_pass(self):
    self.assertEquals(self.logger.logFailure(self.NAME, self.MTYPE, 1), 1)
  
  def test_logIfFail_fail(self):
    self.assertEquals(self.logger.logIfFail(self.NAME, self.MTYPE, 2, 0, self.dummy_func, 4, 2), 0) 

  def test_logIfFail_error(self):
    self.assertEquals(self.logger.logIfFail(self.NAME, self.MTYPE, 2, 0, self.dummy_func, 4, 0), 1)

  def test_logIfFail_pass(self):
    self.assertEquals(self.logger.logIfFail(self.NAME, self.MTYPE, 3, 0, self.dummy_func, 4, 2), 1)

  def test_reportCountEqual_fail(self):
    self.assertEquals(self.logger.reportCountEqual(3, 0, self.dummy_func, 4, 2), 0)

  def test_reportCountEqual_error(self):
    self.assertEquals(self.logger.reportCountEqual(2, 0, self.dummy_func, 4, 0), 1)

  def test_reportCountEqual_pass(self):
    self.assertEquals(self.logger.reportCountEqual(2, 0, self.dummy_func, 4, 2), 1)
  
  def test_reportLatency(self):
    self.assertEquals(self.logger.reportLatency(self.NAME, self.MTYPE, self.dummy_func, 4, 2), 2)

if __name__ == '__main__':
  unittest.main()

