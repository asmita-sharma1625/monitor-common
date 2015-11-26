import sys
import os
import sqlite3
import re
import sys
import shutil
from metricgenerator.common.configReader import ConfigReader

class Consumer:

  suffixpattern = "metric\d{4}-\d{2}-\d{2} [0-2][0-9]:[0-5][0-9]"
  fileextension = ".log"

  class ActionOnFile:
    def doTask(self, filename, relativepath):
      return True

  class DefaultAction(ActionOnFile):
    def __init__(self, target_path):
      self.target_path = target_path

    def doTask(self, filename,relativepath):
      dest_path = os.path.join(self.target_path, os.path.dirname(relativepath))
      try:
        if not os.path.isdir(dest_path):
          os.makedirs(dest_path)
        shutil.copy(filename, dest_path)
      except:
        return False
      return True

  class ObjectStorageAction(ActionOnFile):
    def __init__(self):
      self.username = "account_name:username"
      self.api_key = "API Public key."
      self.authurl = "https::/user.com/auth"
      #self.conn = cloudfiles.get_connection(username=self.username, api_key=self.api_key, authurl=self.authurl)

    def doTask(self, filename, logfilename):
      #if not self.conn
      #  return False
      return True

  def __init__(self, path, deleterotatedfiles=True, logpattern=".*", provider = None, target_path=None):
    self.path = path
    self.deleterotatedfiles = deleterotatedfiles

    self.logpattern = logpattern
    self.regex = re.compile(self.logpattern)

    dest_path = "/tmp/backups/"
    if target_path:
      dest_path = target_path
    if provider:
      self.provider = provider
    else:
      self.provider = Consumer.DefaultAction(dest_path)

  def list_of_logs(self):
    return [os.path.join(dirpath, files) \
              for (dirpath, dirname, filename) in os.walk(self.path) \
              for files in filename if files.endswith(Consumer.fileextension) and self.regex.search(files)]


  def do_action(self, filename, relpath):
    #This is just for test of now. Later, it will be upgraded for object storage.
    return self.provider.doTask(filename, relpath)
    #Temporary just make an entry into the file.

  def do_delete(self, filename):
    os.unlink(filename)

  def consume_each_file(self, filename):
    #Relative path from the given path to maintain hierarchy.
    relpath = os.path.relpath(filename, self.path)
    result = self.do_action(filename, relpath)
    if not result:
      sys.stderr.write("Operation failed on all or some files")
    else:
      if self.deleterotatedfiles:
        self.do_delete(filename)

  def consume(self):
    #Get list of file names
    file_names = self.list_of_logs()
    map(self.consume_each_file, file_names)

if __name__ == '__main__':
  if len(sys.argv) != 3:
    raise SystemExit("Invalid Arguments - config path and section name required")

  CONFIGFILE = sys.argv[1]
  SECTION = sys.argv[2]
  TARGET_PATH = sys.argv[3]
  ConfigReader.setConfig(CONFIGFILE)

  print "CONFIGFILE - ", CONFIGFILE
  print "SECTION - ", SECTION

  LOGDIR =  ConfigReader.getValue(SECTION, "LogDir") #sys.argv[2]
  FILENAME = ConfigReader.getValue(SECTION, "Filename") #sys.argv[3]
  
  consumer = Consumer(LOGDIR, deleterotatedfiles = False, logpattern = FILENAME, target_path = TARGET_PATH)
  consumer.consume()   

