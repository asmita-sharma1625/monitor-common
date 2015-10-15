from logger import logger2
import time

logger = logger2.Logger("demo_logger")

def generate_logs():
  i = 10000
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
