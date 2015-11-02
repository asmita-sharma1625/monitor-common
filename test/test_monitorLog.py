import unittest
from logger.common.monitorLog import monitorLog
from logger.common.handler import Handler

class TestMonitorLog(unittest.TestCase):
  def test_logError(self):
    with self.assertRaises(Exception):
      Handler("dummy", "dummy").getLogHandler()
    print "test passed*******************"
