import sys
import os
import sqlite3
import re
import time, datetime
import shutil, socket
from metricgenerator.common.configReader import ConfigReader
from metricgenerator import s3Dao
import logging, logging.handlers
import sys


log = logging.getLogger('Consumer')
log.addHandler(logging.NullHandler())
log.setLevel(logging.DEBUG)

class Consumer(object):

    def doTask(self, filename,relativepath):
        dest_path = os.path.join(self.target_path, os.path.dirname(relativepath))
        try:
            if not os.path.isdir(dest_path):
                os.makedirs(dest_path)
            shutil.copy(filename, dest_path)
        except:
            return False
        return True

    def __init__(self, path, interval = None, deleterotatedfiles=True, target_path=None):
        log.debug("Consumer instantiated")
        self.path = path
        self.deleterotatedfiles = deleterotatedfiles
        self.archive_path = os.path.join(self.path, "archive")

        if not os.path.exists(self.archive_path):
            os.makedirs(self.archive_path)

        self.current_time = time.time()
        self.interval = int(interval)

        if target_path is not None:
            self.dest_path = target_path
        else:
            self.dest_path = socket.gethostname()

    def list_of_logs(self):
        log.debug("Searching for files")
        list_of_files = []
        for (dirpath, dirname, filename) in os.walk(self.path):
            if "archive" not in dirpath:
                for files in filename:
                    abs_file = os.path.join(dirpath, files)
                    try:
                        log_time = os.path.getmtime(abs_file)
                        time_delta = (self.current_time - log_time) / self.interval
                        if time_delta > 1:
                            list_of_files.append(abs_file)
                    except os.error:
                        log.debug("Error while getting mtime for file : " + abs_file)
                        pass
                    except:
                        log.debug("Error while calculating time delta for file : " + abs_file)
                        pass
        return list_of_files

    def do_action(self, filename, relpath):
        #This is just for test of now. Later, it will be upgraded for object storage.
        return self.doTask(filename, relpath)
        #Temporary just make an entry into the file.

    def do_delete(self, filename):
        os.rename(filename, os.path.join(self.archive_path, os.path.basename(filename)))

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
        log.debug("Files to be consumed : - " + `file_names`)
        map(self.consume_each_file, file_names)


class ObjectStorageConsumer(Consumer):
    def __init__(self, bucket, path, interval = None, deleterotatedfiles=True, target_path=None):
        super(ObjectStorageConsumer, self).__init__(path, interval, deleterotatedfiles, target_path)
        log.debug("Object Store Consumer instantiated")
        self.s3Dao = s3Dao.S3Dao()
        self.s3Dao.setBucket(bucket)

    def doTask(self, filename, logfilename):
        date = datetime.date.today()
        dateRecord = os.path.join(`date.year`, os.path.join(`date.month`, `date.day`))
        logfilename = os.path.join(dateRecord, logfilename)
        if self.dest_path is not None:
            logfilename = os.path.join(self.dest_path, logfilename)
            filename = os.path.join(self.path, filename)
            log.debug("Storing file : " + filename + " @S3 Object Key :" + logfilename)
            try:
                self.s3Dao.uploadObject(logfilename, filename)
            except Exception as error:
                log.error("ERROR : unable to upload " + filename + "to s3", traceback.format_exc())
                pass
        return True


if __name__ == '__main__':
    if len(sys.argv) < 3:
        raise SystemExit("Invalid Arguments - config path, section name and delete_flag required")

    CONFIGFILE = sys.argv[1]
    SECTION = sys.argv[2]

    if len(sys.argv) == 4:
        TARGET_PATH = sys.argv[3]
    else:
        TARGET_PATH = None

    SOURCE_DIR = None
    BUCKET = None
    INTERVAL = None
    LOG_FORMAT = None
    LOGFILE = None

    try:
        configReader = ConfigReader(CONFIGFILE)
    except:
        print "Config file not found", traceback.format_exc()

    try:
        LOG_FORMAT = configReader.getValue(SECTION, "logformat")
        LOGFILE = configReader.getValue(SECTION, "logfile")
        ''' configure logger'''
        formatter = logging.Formatter(LOG_FORMAT)
        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(formatter)
        log.addHandler(ch)
        fh = logging.handlers.RotatingFileHandler(LOGFILE, maxBytes=(1048576*5), backupCount=7)
        fh.setFormatter(formatter)
        log.addHandler(fh)
    except:
        print "Could not configure logger", traceback.format_exc()
        pass

    try:
        SOURCE_DIR =  configReader.getValue(SECTION, "SourceDir")
        BUCKET = configReader.getValue(SECTION, "Bucket")
        try:
            INTERVAL = configReader.getValue(SECTION, "Interval")
        except:
            log.debug("Interval not defined in config")
            pass
    except:
        log.error("Config variables cannot be found")
        raise Exception("Config variables cannot be found")

    log.debug("SOURCE_DIR : " + `SOURCE_DIR`)
    log.debug("BUCKET : " + `BUCKET`)
    log.debug("INTERVAL : " + `INTERVAL`)
    log.debug("LOG_FORMAT : " + `LOG_FORMAT`)
    log.debug("LOGFILE  : " + `LOGFILE`)
    log.debug("TARGET_PATH : " + `TARGET_PATH`)

    log.debug("Instantiating Consumer")
    '''instantiate consumer'''
    consumer = ObjectStorageConsumer(BUCKET, SOURCE_DIR, interval = INTERVAL, target_path = TARGET_PATH)
    consumer.consume()
    log.debug("Consumer finished successfully")
