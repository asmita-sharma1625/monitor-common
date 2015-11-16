import unittest
import re
import socket
from metricgenerator.common.Constants import Constants 

class TestConstants(unittest.TestCase):

  NAME = "demo_name"
  TYPE = "Runtime"
  VALUE_STRING = "Metric Value : 123\n"

  def test_constant (self):
    self.assertEqual(Constants.RUNTIME, self.TYPE)

  def test_getHostname (self):
    self.assertEqual(Constants.getHostname(), socket.gethostname())

  def test_toString (self):
    string = "Metric Name : " + self.NAME + "\n" + "Metric Type : " + self.TYPE + "\n" + self.VALUE_STRING
    self.assertNotEqual(re.match(string, Constants.prependMetricInfo(self.NAME, self.TYPE, self.VALUE_STRING)), None)

if __name__ == '__main__':
  unittest.main()

