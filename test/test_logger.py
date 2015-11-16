import unittest
from metricgenerator import logger
from test import democonfig 

class TestLogger(unittest.TestCase):
  
  SERVICE = "TestLogger"
  NAME = "dummy_metric"
  SEVERITY = 50
  #socket = 5578

  def setUp(self):
    cfgfile = "logconfig.cfg"
    #TestLogger.socket = TestLogger.socket + 1
    #configWriter.CreateConfigFile("Config.cfg", "Constants", "Socket", "tcp://127.0.0.1:"+`TestLogger.socket`)
    #configWriter.CreateConfigFile("Config.cfg", "Constants", "LogDir", "./logs")
    #configWriter.CreateConfigFile("Config.cfg", "Constants", "Filename", "metric.log")
    democonfig.demoConfig(cfgfile).setConfig()
    self.logger = logger.Logger(self.SERVICE, cfgfile)

  def dummy_func(self, a, b):
    return a / b  

  def test_logFailure_fail(self):
    self.assertEquals(self.logger.logFailure(self.NAME, 0, self.SEVERITY), 0)

  def test_logFailure_pass(self):
    self.assertEquals(self.logger.logFailure(self.NAME, 1, self.SEVERITY), 1)
  
  def test_logIfFail_fail(self):
    self.assertEquals(self.logger.logIfFail(self.NAME, 2, 0, self.dummy_func, self.SEVERITY, 4, 2), 0) 

  def test_logIfFail_error(self):
    self.assertEquals(self.logger.logIfFail(self.NAME, 2, 0, self.dummy_func, self.SEVERITY, 4, 0), 1)

  def test_logIfFail_pass(self):
    self.assertEquals(self.logger.logIfFail(self.NAME, 3, 0, self.dummy_func, self.SEVERITY, 4, 2), 1)

  def test_reportCountEqual_fail(self):
    self.assertEquals(self.logger.reportCountEqual(3, 0, self.dummy_func, 4, 2), 0)

  def test_reportCountEqual_error(self):
    self.assertEquals(self.logger.reportCountEqual(2, 0, self.dummy_func, 4, 0), 1)

  def test_reportCountEqual_pass(self):
    self.assertEquals(self.logger.reportCountEqual(2, 0, self.dummy_func, 4, 2), 1)
  
  def test_reportLatency(self):
    self.assertEquals(self.logger.reportLatency(self.NAME, self.dummy_func, self.SEVERITY, 4, 2), 2)

if __name__ == '__main__':
  unittest.main()

