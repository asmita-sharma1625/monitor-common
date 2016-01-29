#from metricgenerator import publish
from metricgenerator import logger
import thread
import unittest
import time
import threading
import traceback

mutex = threading.Lock()

#class MultiThreading:

#publish.setLogger("Test", "config.cfg")
logger = logger.Logger("Test","config.cfg")

#@publish.ReportLatency("multi-thread-latency")
#def print_time(self, threadName, delay):
def print_time( threadName, delay):
  #self.logger.logFailure(threadName, "1")
  #loghandler = logHandler.LogHandler("Test","config.cfg")
  count = 0
  while count < 20:
    #mutex.acquire()
    print"got it=============="+threadName+"="+`count`
    logger.logCount(threadName,count)
    #print "Test "+`count`
    time.sleep(delay)
    count += 1
    #mutex.release()
    #print "%s: %s" % ( threadName, time.ctime(time.time()) )


class TestMultiThreading(unittest.TestCase):

  def test_multithreadedlogger(self):
    #test = MultiThreading()
    try:
      '''
      for i in range(1,5):
        test.print_time("main-thread", 2)
      '''
      thread1=threading.Thread(target=print_time("Thread-1",0))
      thread2= threading.Thread(target=print_time("Thread-2",0))
      thread3= threading.Thread(target=print_time("Thread-3",0))
      thread1.start()
      thread2.start()
      thread3.start()
      '''
      thread.start_new_thread( print_time, ("Thread-1", 0, ) )
      thread.start_new_thread( print_time, ("Thread-2", 0, ) )
      thread.start_new_thread( print_time, ("Thread-3", 0, ) )
      '''
      #thread1.join()
      #thread2.join()
      #thread3.join()
      '''
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
