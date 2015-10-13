#!/usr/bin/python

from logger import rotator
import unittest
import sys
import os
import tempfile
import shutil
import re
import time

class RotatorTest(unittest.TestCase):
  
  def test_rotator(self):
    (tempath,filesize) = self.__create_setup()
    filecount = self.__validate_before(tempath)

    self.assertTrue(filecount > 0)

    mrotator = rotator.Rotator(tempath)
    mrotator.rotate_log_file()

    self.assertTrue(self.__validate_after(tempath, filecount, filecount, filesize))
    self.__tear_setup(tempath)

  def test_rotator_twice_run(self):
    (tempath,filesize) = self.__create_setup()
    filecount = self.__validate_before(tempath)

    self.assertTrue(filecount > 0)

    mrotator = rotator.Rotator(tempath)
    mrotator.rotate_log_file()
    self.assertTrue(self.__validate_after(tempath, filecount, filecount, filesize))

    #Create setup files again
    self.__create_setup_files(tempath)
    self.assertTrue(self.__validate_before(tempath) == filecount)
    time.sleep(1)
    mrotator.rotate_log_file()

    self.assertTrue(self.__validate_after(tempath, filecount, 2*filecount, filesize))
    self.__tear_setup(tempath)
  
  def test_rotator_openedfile(self):
    (tempath, filesize) = self.__create_setup()
    filecount = self.__validate_before(tempath)
    file1 = open(os.path.join(tempath, "conductor_metric.log"), "a")
    file2 = open(os.path.join(tempath, "test_dir/service1_metric.log"), "a")
    mrotator = rotator.Rotator(tempath)
    mrotator.rotate_log_file()
    self.assertTrue(self.__validate_after(tempath, filecount, filecount, filesize))

  def __create_setup(self):
    dirpath = tempfile.mkdtemp()

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


