from logger.logger import Logger
import time

logger = Logger("test_annotation")

@logger.reportLatency("demo", "demo")
def func(a , b):
  time.sleep(5)
  return a / b;

func(4, 2)
