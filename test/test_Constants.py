import unittest
import re
import socket
from logger.common.Constants import Constants 

class TestConstants(unittest.TestCase):

  NAME = "demo_name"
  TYPE = "Runtime"
  TIME = 123

  def test_constant (self):
    self.assertEqual(Constants.RUNTIME, self.TYPE)

  def test_getHostname (self):
    self.assertEqual(Constants.getHostname(), socket.gethostname())

  def test_toString (self):
    string = "Metric Name : " + self.NAME + "\n" + "Metric Type : " + self.TYPE + "\n" + "Metric Value : " + `self.TIME` + "\n"
    self.assertNotEqual(re.match(string, Constants.toStringRuntime(self.NAME, self.TYPE, self.TIME)), None)

if __name__ == '__main__':
  unittest.main()

