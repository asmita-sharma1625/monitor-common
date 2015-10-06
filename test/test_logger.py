import unittest

class TestLogger(unittest.TestCase):

  def test_sample(self):
    self.assertEqual(2+3,5)

  def test_sample2(self):
    self.assertTrue(2+4==6)

  def test_failing(self):
    self.assertFalse(2+4==6)

if __name__ == '__main__':
  unittest.main()

