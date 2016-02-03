from metricgenerator import logger

logger = logger.Logger("Test-1","test-config1.cfg")
customDict = {'a':'b','c':'d'}
class context:
    def __init__(self,a,b,c):
        self.a = a
        self.b = b  
        self.c = c

cntxt = context('a','b','c')

def func(a,b,c):
     print b,c

from metricgenerator import publish
publish = publish.Publish("Test-1","test-config1.cfg")

@publish.ReportLatency("publish-1",20,[['a']])
def f(a,b,c):
    print c,b

logger.reportLatency("latency-1", func, 20, [['a']], cntxt, 5, 2)
logger.logCount("count-1", 5, 20, customDict)
f(cntxt, 5, 2)

import test_service2
logger.reportLatency("test1-latency",test_service2.func, 20, [['b']],cntxt,5,2)
