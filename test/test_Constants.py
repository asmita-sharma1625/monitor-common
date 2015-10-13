import unittest
from logger.common import Constants 

class TestConstants(unittest.TestCase):

  NAME = "demo_name"
  TYPE = "demo_type"  
  TIME = 123

  def test_constant (self):
    self.assertEqual(Constants.Constants.RUNTIME, "Runtime")

  def test_toString (self):
    string = "Name : " + self.NAME + "\n" + "Metric Type : " + self.TYPE + "\n" + "Runtime : " + TIME + "\n"
    self.assertEqual(Constants.Constants.toStringRuntime(NAME, TYPE, TIME) , string)

if __name__ == '__main__':
  unittest.main()

