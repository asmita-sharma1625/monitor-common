#!/usr/bin/python

import unittest
import os
import time
import metricgenerator.common.singleton
import tempfile
import sys

'''class CommonTest(unittest.TestCase):
 
  def test_singleton(self):
    def childprocess():
      singlelock.checkSingleton()
      #Wait for the process for some signal.
      while os.path.isfile(os.path.join(tempath, "newfile")):
        time.sleep(0)

      sys.exit(0)
    singlelock = logger.common.singleton.SingletonProcess("test1")
    tempath = tempfile.mkdtemp()
    open(os.path.join(tempath, "newfile"), "a").close()

    newpid = os.fork()
    if 0 == newpid:
      childprocess()
    else:
      newpid2 = os.fork()
      if 0 == newpid2:
        childprocess()
      else:
        #Wait for second process
        os.remove(os.path.join(tempath, "newfile"))
        (returnid, status) = os.waitpid(newpid2, 0)
        #print "Return id " + str(returnid) + " Status "+str(status)
        self.assertTrue(returnid==newpid2 and status == 256, "Singleton lock failed in the second process")
        
        #Create another new process and it should pass
        os.waitpid(newpid, 0)
        newpid3 = os.fork()
        if newpid3==0:
          childprocess()
        else:
          (returnid, status) = os.waitpid(newpid3, 0)
          print "Return id " + str(returnid) + " Status "+str(status)
          self.assertTrue(returnid==newpid3 and status==0, "Singleton lock failed in the third process when it should succeed")
'''
