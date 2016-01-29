import unittest
from metricgenerator import logger
#from test import democonfig 

class TestLogger(unittest.TestCase):
  
  SERVICE = "Test"
  NAME = "logger_metric"
  SEVERITY = 50
  #socket = 5578
  
  logger = logger.Logger(SERVICE, "config.cfg")

  def setUp(self):
    '''
    TestLogger.socket = TestLogger.socket + 1
    configWriter.CreateConfigFile("Config.cfg", "Constants", "Socket", "tcp://127.0.0.1:"+`TestLogger.socket`)
    configWriter.CreateConfigFile("Config.cfg", "Constants", "LogDir", "./logs")
    configWriter.CreateConfigFile("Config.cfg", "Constants", "Filename", "metric.log")
    '''
    '''
    cfgfile = "logconfig.cfg"
    democonfig.demoConfig(cfgfile).setConfig()
    '''
    #TestLogger.logger = logger.Logger(self.SERVICE, cfgfile)

  def dummy_func(self, a, b):
    return a / b  

  def test_logFailure_fail(self):
    print "1 log instance :", `logger`
    self.assertEquals(TestLogger.logger.logFailure(self.NAME, 0, self.SEVERITY), 0)

  def test_logFailure_pass(self):
    print "2 log instance :", `logger`
    self.assertEquals(TestLogger.logger.logFailure(self.NAME, 1, self.SEVERITY), 1)
  
  def test_logIfFail_fail(self):
    print "3 log instance :", `logger`
    self.assertEquals(TestLogger.logger.logIfFail(self.NAME, 2, 0, self.dummy_func, self.SEVERITY, 4, 2), 0) 

  def test_logIfFail_error(self):
    print "4 log instance :", `logger`
    self.assertEquals(TestLogger.logger.logIfFail(self.NAME, 2, 0, self.dummy_func, self.SEVERITY, 4, 0), 1)

  def test_logIfFail_pass(self):
    print "5 log instance :", `logger`
    self.assertEquals(TestLogger.logger.logIfFail(self.NAME, 3, 0, self.dummy_func, self.SEVERITY, 4, 2), 1)

  def test_reportCountEqual_fail(self):
    print "6 log instance :", `logger`
    self.assertEquals(TestLogger.logger.reportCountEqual(3, 0, self.dummy_func, 4, 2), 0)

  def test_reportCountEqual_error(self):
    print "7 log instance :", `logger`
    self.assertEquals(TestLogger.logger.reportCountEqual(2, 0, self.dummy_func, 4, 0), 1)

  def test_reportCountEqual_pass(self):
    self.assertEquals(TestLogger.logger.reportCountEqual(2, 0, self.dummy_func, 4, 2), 1)
  
  def test_reportLatency(self):
    self.assertEquals(TestLogger.logger.reportLatency(self.NAME, self.dummy_func, self.SEVERITY, 4, 2), 2)

  def test_logCount(self):
    for i in range(1,10):
      print "--------------logging count----------------"
      TestLogger.logger.logCount("***count***",20)

if __name__ == '__main__':
  unittest.main()

