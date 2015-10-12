import unittest
import re
import os
from logger.logHandler import LogHandler 
from logger.common.Constants import Constants

class TestLogHandler(unittest.TestCase):

  SERVICE = "demo_service"
  EXPECTED_STRING = "Region : demo_region\nZone : demo_zone\nHost : demo_host\n"
  FILENAME = "metric.log"
  MSG = "demo_msg"

  def setUp(self):
    self.logHandler = LogHandler(TestLogHandler.SERVICE) 

  def test_dirIfNotExists(self):
    self.assertTrue(os.path.exists(Constants.LOGDIR + "/" + TestLogHandler.SERVICE))

  def test_dirIfExists(self):
    new_logHandler = LogHandler(TestLogHandler.SERVICE)
    self.assertTrue(os.path.exists(Constants.LOGDIR + "/" + TestLogHandler.SERVICE))

  def test_filepath(self):
    self.assertTrue(os.path.exists(Constants.LOGDIR + "/" + TestLogHandler.SERVICE + "/" + TestLogHandler.FILENAME))

  def test_appendLog(self):
    self.logHandler.appendLog(TestLogHandler.MSG)
    fileHandler = open(Constants.LOGDIR + "/" + TestLogHandler.SERVICE + "/" + TestLogHandler.FILENAME)
    self.assertNotEqual(re.search(TestLogHandler.MSG, fileHandler.read()), None)

if __name__ == '__main__':
  unittest.main()

