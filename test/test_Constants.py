import unittest
import re
from logger.common.Constants import Constants 

class TestConstants(unittest.TestCase):

  NAME = "demo_name"
  TYPE = "demo_type"  
  TIME = 123

  def test_constant (self):
    self.assertEqual(Constants.RUNTIME, "Runtime")

  def test_toString (self):
    string = "Name : " + self.NAME + "\n" + "Metric Type : " + self.TYPE + "\n" + "Runtime : " + `self.TIME` + "\n"
    self.assertNotEqual(re.match(string, Constants.toStringRuntime(self.NAME, self.TYPE, self.TIME)), None)

if __name__ == '__main__':
  unittest.main()

