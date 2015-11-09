from logger.consumer import Consumer
from logger.common.Constants import Constants
import unittest
import filecmp
from test.demo_config import demoConfig
import os 

class TestConsumerIntegrationWithLogger(unittest.TestCase):

  def setUp(self):
    cfgfile = demoConfig().setConfig()  
    self.src_path = "../logs"
    self.dest_path = "../consumer"

  @unittest.skipUnless(os.path.exists(os.path.join("../logs", Constants.getHostname())), "logger test case not run yet")
  def test_logConsumption(self):
    #configWriter.CreateConfigFile("config.cfg", "Constants", "LogDir", "./logs")
    #ConfigReader.setConfig("config.cfg")
    print "---------------integration test for consumer running -----------------"
    consumer = Consumer(self.src_path , deleterotatedfiles = False, logpattern = "metric.*\.log", target_path = self.dest_path)
    consumer.consume() 
    diff = filecmp.dircmp(self.src_path, self.dest_path)
    self.assertEquals(diff.left_list, diff.right_list)
