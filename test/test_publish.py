import unittest
from metricgenerator import logger, publish
import time
#from test import democonfig 

class TestPublish(unittest.TestCase): 

  SERVICE = "Test"
  publish = publish.Publish(SERVICE)

  def setUp(self):
    #cfgfile = "config.cfg"
    '''
    configWriter.CreateConfigFile("pconfig.cfg", "Constants", "Socket", "tcp://127.0.0.1:8932")
    configWriter.CreateConfigFile("pconfig.cfg", "Constants", "LogDir", "./logs")
    configWriter.CreateConfigFile("pconfig.cfg", "Constants", "Filename", "metric.log")
    '''
    #democonfig.demoConfig(cfgfile).setConfig()
    #publish = publish.Publish("demo_publish", cfgfile)
 
  def test_ReportLatency(self):
    print "testing publish"
    i = 10
    j = 2
    while i > 0:
      self.demo_action(j * 2, j)
      i = i - 1
      j = j * 2

  @publish.ReportLatency("publish", 40)
  def demo_action(self, a, b):
    print "in demo_action"
    time.sleep(1)
    return a / b
 
if __name__ == '__main__':
  unittest.main()
  test = TestPublish()
  test.test_ReportLatency()
