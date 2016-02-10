#from metricgenerator import publish
from metricgenerator import logger
import threading
import unittest
import time
import traceback

class MultiThreading:

  #publish = publish.Publish("Test", "config.cfg")
  logger = logger.Logger("Test","config.cfg")

  #@publish.ReportLatency("multi-thread-latency")
  def print_time(self, threadName, delay):
    #self.logger.logFailure(threadName, "1")
    count = 0
    while count < 5:
      self.logger.logFailure(threadName, "1")
      time.sleep(delay)
      count += 1
      #print "%s: %s" % ( threadName, time.ctime(time.time()) )


class TestMultiThreading(unittest.TestCase):

  def test_multithreadedlogger(self):
    test = MultiThreading()
    threads = []
    try:
      for i in range(1,9):
        threads.append(threading.Thread(target=test.print_time("Thread-"+`i`, 0)))
      for i in range(1,9):
        threads.pop().start()
      '''
      thread.start_new_thread( test.print_time, ("Thread-1", 0, ) )
      thread.start_new_thread( test.print_time, ("Thread-2", 0, ) )
      thread.start_new_thread( test.print_time, ("Thread-3", 0, ) )
      thread.start_new_thread( test.print_time, ("Thread-4", 0, ) )
      thread.start_new_thread( test.print_time, ("Thread-5", 0, ) )
      thread.start_new_thread( test.print_time, ("Thread-6", 0, ) )
      thread.start_new_thread( test.print_time, ("Thread-7", 0, ) )
      thread.start_new_thread( test.print_time, ("Thread-8", 0, ) )
      '''
    except:
      print "Error: unable to start thread",traceback.format_exc()

if __name__ == '__main__':
  unittest.main()
  test = TestMultiThreading()
  test.test_multithreadedlogger()
  #for i in range(1,5):
    #thread.start_new_thread( MultiThreading().print_time, ("Thread - " + i, 0, ) )
