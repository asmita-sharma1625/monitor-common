#from metricgenerator import publish
from metricgenerator import logger
from multiprocessing import Process
import unittest
import time

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
    processes = []
    for i in range(1,9):
      processes.append(Process(target=test.print_time, args=("Process-"+`i`, 0,)))
    for i in range(1,9):
      processes.pop().start()

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

if __name__ == '__main__':
  unittest.main()
  test = TestMultiThreading()
  test.test_multithreadedlogger()
  #for i in range(1,5):
    #thread.start_new_thread( MultiThreading().print_time, ("Thread - " + i, 0, ) )
