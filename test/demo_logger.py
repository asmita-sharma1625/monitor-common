from logger import logger, publish
import time
 
#logger = logger.Logger("demo_logger")
publish.setLogger("demo_publish")

def generate_logs():
  i = 10000
  j = 2
  while i > 0:
    demo_log(j * 2, j)
    i = i - 1
    j = j * 2

@publish.ReportLatency("demo", "demo")
def demo_log(a, b):
  #logger.reportLatency("report latency", "demo-metric", demo_action, a, b)
  return demo_action(a, b)

def demo_action(a, b):
  time.sleep(5)
  return a / b
  
generate_logs()
