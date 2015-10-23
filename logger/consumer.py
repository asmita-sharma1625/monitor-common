
import os
import sqlite3
import re
import sys
import shutil

class Consumer:

  suffixpattern = "\d{4}-\d{2}-\d{2} [0-2][0-9]:[0-5][0-9]"
  fileextension = "metric.log"

  class LastFileInfo:
    infopath = "/tmp/lib/jiocloud-consumer/consumer.db"

    def open_fileinfos(self):
      create_new = False
      if not os.path.isfile(Consumer.LastFileInfo.infopath):
        if not os.path.isdir(os.path.dirname(Consumer.LastFileInfo.infopath)):
          os.makedirs(os.path.dirname(Consumer.LastFileInfo.infopath))
        open(Consumer.LastFileInfo.infopath, "w").close()
        create_new = True

      self.sqliteconnection = sqlite3.connect(Consumer.LastFileInfo.infopath)
      #Case where database is being created first time, table must be created.
      if create_new:
        c = self.sqliteconnection.cursor()
        c.execute("CREATE TABLE lastfiles (filename text primary key, lastfile text)")
        self.sqliteconnection.commit()

    def close_fileinfos(self):
      self.sqliteconnection.close()

    def get_last_file(self, name):
      filename = os.path.basename(name)
      cur = self.sqliteconnection.cursor()
      #print "SELECT lastfile from lastfiles where filename='%s'"%(filename,)
      cur.execute("SELECT lastfile from lastfiles where filename='%s'"%(filename,))
      rows = cur.fetchone()
      #print "Rows " + `rows`
      if rows:
        return rows[0]

      cur.execute("INSERT INTO lastfiles (filename) VALUES('%s')"%(filename,))
      self.sqliteconnection.commit()
      return ""

    def set_last_file(self, name, lastfilename):
      filename = os.path.basename(name)
      lastfile = os.path.basename(lastfilename)
      cur = self.sqliteconnection.cursor()
      cur.execute("UPDATE lastfiles SET lastfile='%s' WHERE filename ='%s'"%(lastfile, filename))
      self.sqliteconnection.commit()

  class ActionOnFile:
    def doTask(self, filename,logfilename):
      return True

  class DefaultAction(ActionOnFile):
    def __init__(self, target_path):
      self.target_path = target_path

    def doTask(self, filename,logfilename):
      dest_path = os.path.join(self.target_path, os.path.splitext(os.path.basename(logfilename))[0])
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

  #def __init__(self, path, '''consumeinterval, ''' deleterotatedfiles=True, logpattern="", lastfileinfo=None):
  def __init__(self, path, deleterotatedfiles=True, logpattern="", provider = None, target_path=None, lastfileinfo=None):
    self.path = path
#    self.consumerinterval = consumerinterval # Now it seems unneeded.
    self.deleterotatedfiles = deleterotatedfiles
    if lastfileinfo:
      self.lastfileinfo = lastfileinfo
    else:
      self.lastfileinfo = Consumer.LastFileInfo()

    if logpattern != "":
      self.logpattern = logpattern
    else:
      self.logpattern = Consumer.suffixpattern
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
              for files in filename if files.endswith(Consumer.fileextension)]

  def list_of_consumeables(self, filename):
    '''
      How to get list consumable files
      1. Estimate the last run time and picks file after that time.
      2. Get the last file which was processed. And filter out the files greater than that file. And update the file with increasing time.
      Currently using method 2. Sqlite3 database is being used to
    '''
    fileprefix = os.path.basename(filename)
    lastfilename = self.lastfileinfo.get_last_file(filename)
    if lastfilename == "":
      lastfilename = fileprefix

    return sorted([os.path.join(dirpath, files) \
              for (dirpath, _, filenames) in os.walk(os.path.dirname(filename)) \
              for files in filenames if self.regex.search(files) and files.startswith(fileprefix) and files > lastfilename])
    #Update the data with the last file.
    #self.lastfileinfo.set_last_file(filename, filelists[-1])
    #return filelists


  def do_action(self, last_value, filename):
    #This is just for test of now. Later, it will be upgraded for object storage.
    return last_value and self.provider.doTask(filename, self.currentlog)
    #Temporary just make an entry into the file.

  def do_delete(self, filename):
    os.unlink(filename)

  def consume_each_file(self, filename):
    files = self.list_of_consumeables(filename)
    #print "Select files for "+filename+" ",
    #print "Files "+`files`
    #This means files are not produced so far.
    if len(files) < 1:
      return
    self.currentlog = filename
    result = reduce(self.do_action, files, True)
    if not result:
      sys.stderr.write("Operation failed on all or some files")
    else:
      self.lastfileinfo.set_last_file(filename, files[-1])
      if self.deleterotatedfiles:
        map(self.do_delete, files)

  def consume(self):
    #Get list of file names
    file_names = self.list_of_logs()

    #For each file name, get list of the files to consume
    self.lastfileinfo.open_fileinfos()
    map(self.consume_each_file, file_names)
    self.lastfileinfo.close_fileinfos()

