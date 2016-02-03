from metricgenerator import logger
logger = logger.Logger("Test-2","test-config2.cfg")
customDict = {'a':'b','c':'d'}
class context:
  def __init__(self,a,b,c):
    self.a = a
    self.b = b  
    self.c = c

cntxt = context('a','b','c')

def func(a,b,c):
     print b,c
logger.reportLatency("latency-2", func, 20, [['a']], cntxt, 5, 2)
logger.logCount("count-2", 5, 20, customDict)

from metricgenerator import publish
publish = publish.Publish("Test-2","test-config2.cfg")

@publish.ReportLatency("publish-2",20,[['a']])
def f(a,b,c):
  print c,b

f(cntxt, 5, 2)
