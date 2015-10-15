from logger import logger
import time

logger = logger.Logger("demo_logger")

def generate_logs():
  i = 10000000
  j = 2
  while i > 0:
    demo_log(j, j*2)
    i = i - 1

def demo_log(a, b):
  logger.reportLatency("report latency", "demo-metric", demo_action, a, b)

def demo_action(a, b):
  time.sleep(5)
  return a / b
  
generate_logs()
