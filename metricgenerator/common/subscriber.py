import sys
import os
import socket
from logbook.queues import ZeroMQSubscriber
from logbook import TimedRotatingFileHandler
#from nova.logger.common import Constants
from metricgenerator.common.configReader import ConfigReader
import zmq

if len(sys.argv) != 3:
    raise SystemExit("Invalid Arguments - config path and section name required")

CONFIGFILE = sys.argv[1]
SECTION = sys.argv[2]
ConfigReader.setConfig(CONFIGFILE)
#mySocket = ConfigReader.getValue("Constants", "Socket")

print "CONFIGFILE - ", CONFIGFILE
print "SECTION - ", SECTION

SERVICE = ConfigReader.getValue(SECTION, "Service") #sys.argv[1]
LOGDIR =  ConfigReader.getValue(SECTION, "LogDir") #sys.argv[2]
FILENAME = ConfigReader.getValue(SECTION, "Filename") #sys.argv[3]
SOCKET = ConfigReader.getValue(SECTION, "Socket") #sys.argv[4]
HOSTNAME = socket.gethostname()

print "SERVICE - ", SERVICE
print "LOGDIR - ", LOGDIR
print "FILENAME - ", FILENAME
print "SOCKET - ", SOCKET
print "HOSTNAME - ", HOSTNAME

subscriber = None

try:
    subscriber = ZeroMQSubscriber(SOCKET, multi = True)
    print "Subscriber bind to socket - ", SOCKET
except zmq.error.ZMQError as error:
    print "error in service " + SERVICE + " while binding to socket :" + SOCKET
    raise zmq.error.ZMQError("error in service " + SERVICE + " while binding to socket :" + SOCKET)
path = os.path.join(os.path.join(LOGDIR, HOSTNAME), SERVICE)
path_with_filename = os.path.join(path, FILENAME)
print "PATH - ", path

if not os.path.exists(path):
    os.makedirs(path)

with TimedRotatingFileHandler(path_with_filename, date_format='%Y-%m-%d %H:%M'):
    #print "Log Received - ", subscriber.recv().message
    subscriber.dispatch_forever()

