import unittest
from metricgenerator.common.monitorLog import monitorLog
from metricgenerator.logger import Logger
from metricgenerator.common.exceptions import IncorrectConfigException

class TestMonitorLog(unittest.TestCase):

  @unittest.skip("skip")
  def test_logError(self):
    with self.assertRaises(IncorrectConfigException):
      Logger("dummy", "dummy.cfg")
    print "test passed*******************"
