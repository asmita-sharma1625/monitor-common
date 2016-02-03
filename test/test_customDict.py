from metricgenerator import logger
logger = logger.Logger("Test","config.cfg")
context = {'a':'b','c':'d'}

def func(a,b,c):
     print b,c
l2 = []
l2.append([])
l1 =[]
l1.append(0)
l2[0].append("a")
logger.reportLatency("new", func, 20, l1, l2, context, 5, 2)

