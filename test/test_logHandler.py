import unittest
from logger import logHandler 


class TestLogHandler(unittest.TestCase):

  HOST = "demo_host"
  ZONE = "demo_zone"
  REGION = "demo_region"
  EXPECTED_STRING = ""
  FILENAME = 

  def setUp(self):
	self.logHandler = LogHandler(TestLogHandler.HOST, TestLogHandler.ZONE, TestLogHandler.REGION) 

  def test_dir(self):
 	self.assertTrue(os.path.exists("/"+TestLogHandler.HOST))

  def test_file(self):
	self.assertTrue(os.path.exists("/"+TestLogHandler.HOST+"/"+TestLogHandler.FILENAME))


if __name__ == '__main__':
	unittest.main()

