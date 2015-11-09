import unittest
from logger.common.monitorLog import monitorLog
from logger.logger import Logger
from logger.common.exceptions import IncorrectConfigException

class TestMonitorLog(unittest.TestCase):

  @unittest.skip("skip")
  def test_logError(self):
    with self.assertRaises(IncorrectConfigException):
      Logger("dummy", "dummy.cfg")
    print "test passed*******************"
