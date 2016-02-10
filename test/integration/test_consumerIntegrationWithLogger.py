from metricgenerator.consumer import Consumer
from metricgenerator.common.Constants import Constants
import unittest
import filecmp
#from test import democonfig 
import os 
import socket

class TestConsumerIntegrationWithLogger(unittest.TestCase):

  def setUp(self):
    '''
    cfgfile = "iconfig.cfg"
    cfgfile = democonfig.demoConfig(cfgfile).setConfig() 
    ''' 
    self.src_path = "../logs"
    self.dest_path = "../consumer"

  @unittest.skipUnless(os.path.exists("../logs"), "logger test case not run yet")
  def test_logConsumption(self):
    #configWriter.CreateConfigFile("config.cfg", "Constants", "LogDir", "./logs")
    #ConfigReader.setConfig("config.cfg")
    print "---------------integration test for consumer running -----------------"
    consumer = Consumer(self.src_path , deleterotatedfiles = False, logpattern = "metric.*\.log", target_path = self.dest_path)
    consumer.consume() 
    diff = filecmp.dircmp(self.src_path, self.dest_path)
    print "diff", diff
    print "left diff", diff.left_list
    print "right diff", diff.right_list
    self.assertEquals(diff.left_list[1:], diff.right_list)
