import sys
import os
import sqlite3
import re
import sys, time, datetime
import shutil, socket
from metricgenerator.common.configReader import ConfigReader
from metricgenerator import s3Dao

class Consumer:

    suffixpattern = "metric\d{4}-\d{2}-\d{2} [0-2][0-9]:[0-5][0-9]"
    fileextension = -1

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
        def __init__(self, bucket, logdir, dest_path = None):
            '''
            self.username = "account_name:username"
            self.api_key = "API Public key."
            self.authurl = "https::/user.com/auth"
            #self.conn = cloudfiles.get_connection(username=self.username, api_key=self.api_key, authurl=self.authurl)
            '''
            self.logdir = logdir
            if dest_path is  not None:
                self.dest_path = dest_path
            else:
                self.dest_path = socket.gethostname()
            print "dest path:", dest_path
            self.s3Dao = s3Dao.S3Dao()
            self.s3Dao.setBucket(bucket)

        def doTask(self, filename, logfilename):
            date = datetime.date.today()
            print date
            dateRecord = os.path.join(`date.year`, os.path.join(`date.month`, `date.day`))
            print dateRecord
            logfilename = os.path.join(self.dest_path, os.path.join(dateRecord, logfilename)) 
            filename = os.path.join(self.logdir, filename)

            print logfilename, "*******", filename
            try:
                #print "##########", os.stat(filename)[ST_MODE]
                #os.chmod(os.path.dirname(filename), 777)
                self.s3Dao.uploadObject(logfilename, filename)
            except Exception as error:
                print "ERROR : unable to upload " + filename + "to s3"
                pass
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
        '''
        return [os.path.join(dirpath, files) \
                            for (dirpath, dirname, filename) in os.walk(self.path) \
                            for files in filename if files.endswith(Consumer.fileextension) and self.regex.search(files)]
        '''
        list_of_files = []
        fileextension = -1
        for (dirpath, dirname, filename) in os.walk(self.path):
            for files in filename:
                try:
                    fileextension = int(files.rsplit(".",1)[1])
                except:
                    pass
                if self.regex.search(files) and (fileextension > Consumer.fileextension):
                    Consumer.fileextension = fileextension
                    if fileextension == 59:
                        Consumer.fileextension = -1
                    list_of_files.append(os.path.join(dirpath, files))
            return list_of_files

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
    if len(sys.argv) < 4:
        raise SystemExit("Invalid Arguments - config path, section name and delete_flag required")

    CONFIGFILE = sys.argv[1]
    SECTION = sys.argv[2]
    DELETE_FLAG = sys.argv[3]

    if len(sys.argv) == 5:
        TARGET_PATH = sys.argv[4]
    else:
        TARGET_PATH = None
    configReader = ConfigReader(CONFIGFILE)

    print "CONFIGFILE - ", CONFIGFILE
    print "SECTION - ", SECTION

    LOGDIR =  configReader.getValue(SECTION, "LogDir")
    BUCKET = configReader.getValue(SECTION, "Bucket")
    PATTERN = ".*\.log.[0-9]+"

    consumer = Consumer(LOGDIR, deleterotatedfiles = eval(DELETE_FLAG), logpattern = PATTERN, target_path = TARGET_PATH, provider = Consumer.ObjectStorageAction(BUCKET, LOGDIR, TARGET_PATH))
    while 1:
        consumer.consume()
