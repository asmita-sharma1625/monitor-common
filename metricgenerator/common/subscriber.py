import sys
import os, datetime
import socket
import statsd
import zmq
import json
from logbook.queues import ZeroMQSubscriber
from logbook import TimedRotatingFileHandler
from logbook.base import dispatch_record
#from nova.logger.common import Constants
from metricgenerator.common.configReader import ConfigReader
from metricgenerator.common.Constants import Constants

if len(sys.argv) != 3:
    raise SystemExit("Invalid Arguments - config path and section name required")

CONFIGFILE = sys.argv[1]
SECTION = sys.argv[2]
configReader = ConfigReader(CONFIGFILE)
#mySocket = ConfigReader.getValue("Constants", "Socket")

print "CONFIGFILE - ", CONFIGFILE
print "SECTION - ", SECTION

LOGDIR =  configReader.getValue(SECTION, "LogDir") #sys.argv[2]
FILENAME = configReader.getValue(SECTION, "Filename") #sys.argv[3]
SOCKET = configReader.getValue(SECTION, "Socket") #sys.argv[4]

print "LOGDIR - ", LOGDIR
print "FILENAME - ", FILENAME
print "SOCKET - ", SOCKET

subscriber = None

c = statsd.StatsClient('localhost', 8125)
def parseEmitMetrics (msg):
    customDict = json.loads(msg)
    metricName = customDict[Constants.SERVICE] + "." + \
            customDict[Constants.METRIC_NAME]
    #initializing statsd client (search from collectd on which port stasd is
    #running)
    if customDict[Constants.METRIC_TYPE] == Constants.RUNTIME:
        c.timing(metricName, customDict[Constants.METRIC_VALUE])
    elif customDict[Constants.METRIC_TYPE] == Constants.COUNT:
        c.incr(metricName)
'''
def  check_rotation (handler):
    files_to_rotate = handler.files_to_delete()
    if len(files_to_rotate) != 0:
        print "NOT NULL : ", files_to_rotate
        for obj in files_to_rotate:
            fileobj = obj[1]
            os.rename(fileobj, fileobj + "." + `datetime.datetime.now().minute`)
'''
try:
    subscriber = ZeroMQSubscriber(SOCKET, multi = True)
    print "Subscriber bind to socket - ", SOCKET
except zmq.error.ZMQError as error:
    print "error while binding to socket :" + SOCKET
    raise zmq.error.ZMQError("error while binding to socket :" + SOCKET)
path = LOGDIR
path_with_filename = os.path.join(path, FILENAME)
print "PATH - ", path

if not os.path.exists(path):
    os.makedirs(path)

handler = TimedRotatingFileHandler(path_with_filename, date_format='%Y_%m_%d_%H_%M')#, backup_count = 5) #60)

with handler:
    while 1:
        record = subscriber.recv()
        print "Log Received - ", record.message
        parseEmitMetrics(record.message)
        #subscriber.dispatch_forever()
        dispatch_record(record)
        #check_rotation(handler)
