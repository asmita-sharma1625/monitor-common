from metricgenerator import logger
logger = logger.Logger("Test","config.cfg")
customDict = {'a':'b','c':'d'}
class context:
  def __init__(self,a,b,c):
    self.a = a
    self.b = b  
    self.c = c

cntxt = context('a','b','c')

def func(a,b,c):
     print b,c
logger.reportLatency("latency", func, 20, [['a']], cntxt, 5, 2)
logger.logCount("count", 5, 20, customDict)

from metricgenerator import publish
publish = publish.Publish("Test","config.cfg")

@publish.ReportLatency("publish",20,[['a']])
def f(a,b,c):
  print c,b

f(cntxt, 5, 2)
