import unittest
import logger

class TestLogger(unittest.TestCase):
  
  SERVICE = "TestLogger"
  NAME = "dummy_metric"
  MTYPE = "debug"

  def setUp(self):
    self.logger = Logger(self.SERVICE)

  def dummy_func(self, a, b):
    return a / b  

  def test_logIfFail_fail(self):
    AssertEquals(self.logger.logIfFail(self.NAME, self.MTYPE, 2, 0, self.dummy_func, 4, 2), 0) 

  def test_logIfFail_error(self):
    AssertEquals(self.logger.logIfFail(self.NAME, self.MTYPE, 2, 0, self.dummy_func, 4, 0), 1)

  def test_logIfFail_pass(self):
    AssertEquals(self.logger.logIfFail(self.NAME, self.MTYPE, 3, 0, self.dummy_func, 4, 2), 1)

  def test_reportCountEqual_fail(self):
    AssertEquals(self.logger.reportCountEqual(self.NAME, self.MTYPE, 3, 0, self.dummy_func, 4, 2), 0)

  def test_reportCountEqual_error(self):
    AssertEquals(self.logger.reportCountEqual(self.NAME, self.MTYPE, 2, 0, self.dummy_func, 4, 0), 1)

  def test_reportCountEqual_pass(self):
    AssertEquals(self.logger.reportCountEqual(self.NAME, self.MTYPE, 2, 0, self.dummy_func, 4, 2), 1)
  
  def test_reportLatency(self):
    AssertEquals(self.logger.reportLatency(self.NAME, self.MTYPE, self.dummy_func, 4, 2), 2)

if __name__ == '__main__':
  unittest.main()

