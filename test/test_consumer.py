#!/usr/bin/python

from logger import consumer
from logger import rotator
import unittest
import sys
import os
import tempfile
import shutil
import re
import time

class ConsumerTest(unittest.TestCase):

  class FileAction(consumer.Consumer.ActionOnFile):
    def doTask(self, filename, logfilename):
      myfile = open("/tmp/consumer.log","a")
      myfile.write(logfilename+': '+filename+"\n")
      return True 

  def test_consumer(self):
    (tempath,filesize) = self.__create_setup()
    filecount = self.__validate_before(tempath)
    os.unlink(consumer.Consumer.LastFileInfo.infopath)
    logfiles = "/tmp/consumer.log"
    os.unlink(logfiles)
    self.assertTrue(filecount > 0)

    mrotator = rotator.Rotator(tempath)
    mrotator.rotate_log_file()
    time.sleep(2)
    self.__create_setup_files(tempath) 
    mrotator.rotate_log_file()
    time.sleep(1)
    self.__create_setup_files(tempath) 
    mrotator.rotate_log_file()
    time.sleep(1)
    self.__create_setup_files(tempath) 
    mrotator.rotate_log_file()
    mconsumer = consumer.Consumer(tempath,True,"[0-9]+$", None, ConsumerTest.FileAction())
    mconsumer.consume()
    self.assertTrue(self.__wc_l(logfiles) == 20)
    self.__create_setup_files(tempath)
    time.sleep(1)
    mrotator.rotate_log_file()
    mconsumer.consume()
    self.assertTrue(self.__wc_l(logfiles) == 25)
    self.__create_setup_files(tempath)
    time.sleep(1)
    mconsumer.consume()
    self.assertTrue(self.__wc_l(logfiles) == 25)
    time.sleep(1)
    mrotator.rotate_log_file()
    mconsumer.consume()
    self.assertTrue(self.__wc_l(logfiles) == 30)
    #self.assertTrue(self.__validate_after(tempath, filecount, filecount, filesize))
    self.__tear_setup(tempath)

  def __wc_l(self, filename):
    return open(filename, "r").read().count('\n')
  
  def __create_setup(self):
    dirpath = tempfile.mkdtemp()
    #print "Directory path " + dirpath
    #Create a directory and two files inside it
    os.makedirs(os.path.join(dirpath, "test_dir"))
    filesize = self.__create_setup_files(dirpath)
    return (dirpath, filesize)

  def __create_setup_files(self, dirpath):
    self.__write_contents(os.path.join(dirpath, "test_dir/mointor1_metric.log"))
    self.__write_contents(os.path.join(dirpath, "test_dir/service1_metric.log"))
    self.__write_contents(os.path.join(dirpath, "test_dir/service2_metric.log"))
    
    #Create a file
    self.__write_contents(os.path.join(dirpath, "conductor_metric.log"))
    filesize = self.__write_contents(os.path.join(dirpath, "database_metric.log"))
    return filesize

  def __write_contents(self, filename):
    text_file = open(filename, "a")
    text_file.write("some random content is here\nSome more content\nIt should be atomic here\nTest log\n")
    text_file.write("some random content is here\nAgain more content\n")
    text_file.close()
    return os.stat(filename).st_size

  def __tear_setup(self, dirpath):
    shutil.rmtree(dirpath)

  def __validate_before(self, dirpath):
    return len([files for (dirp,dirname,filename) in os.walk(dirpath) for files in filename if files.endswith(rotator.Rotator.fileextension)])

  def __validate_after(self, dirpath, prevcount, rotatedcount, prevsize):
    #matcher = re.compile(r"_metric\.log\.[0-9]+\-[0-9]+\-[0-9]+_[0-9]+\-[0-9]+$")
    matcher = re.compile(r"_metric\.log\.[0-9]+$")
    #print "List 1 " + str([files for (dirp,dirname,filename) in os.walk(dirpath) for files in filename if matcher.search(files) and os.stat(os.path.join(dirp,files)).st_size==prevsize])
    #print "List 2 " + str([files for (dirp,dirname, filename) in os.walk(dirpath) for files in filename if files.endswith(rotator.Rotator.fileextension) and os.stat(os.path.join(dirp,files)).st_size==0])
    return len([files for (dirp,dirname,filename) in os.walk(dirpath) \
                  for files in filename if matcher.search(files) and os.stat(os.path.join(dirp,files)).st_size==prevsize]) == rotatedcount \
                and \
          len([files for (dirp,dirname, filename) in os.walk(dirpath) \
                  for files in filename if files.endswith(rotator.Rotator.fileextension) and os.stat(os.path.join(dirp,files)).st_size==0])==prevcount


