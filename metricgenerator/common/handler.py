import os
import logging
from metricgenerator.common.Constants import Constants
from logbook.compat import RedirectLoggingHandler
from metricgenerator.common.zeroMQHandler import MyZeroMQHandler
from metricgenerator.common.configReader import ConfigReader
from metricgenerator.common.monitorLog import monitorLog
import zmq
''' not used since subscriber is an independent process now '''
'''
from metricgenerator.common.zeroMQSubscriber import MyZeroMQSubscriber
from multiprocessing import Process
import atexit
'''

class Handler:

    childProcess = None

    def __init__(self, service, configFile):
        self.constants = Constants(configFile)
        try:
            self.directory = os.path.join(self.constants.getLogDir(), os.path.join(Constants.getHostname(), service))
        except Exception, error:
            monitorLog.logError("Could not retrieve logging directory", error)
            raise Exception("Could not retrieve logging directory")
        if not os.path.exists(self.directory):
                os.makedirs(self.directory)
        self.service = service
        self.logger = logging.getLogger(self.service)
        self.logger.setLevel(logging.INFO)
        self.logger.addHandler(RedirectLoggingHandler())
        self.socket = self.constants.getSocket()
        #self.context = zmq.Context()

    def getLogHandler(self):
        logger = logging.getLogger(self.service)
        return logger


    def getQueueHandler(self):
        context = zmq.Context()
        return MyZeroMQHandler(self.socket, context).getZeroMQHandler()

    ''' Follwing methods are not used since subscriber is an independent process now '''
    '''
    def startQueueSubscriber(self):
        self.childProcess = Process(target = self.getQueueSubscriber)
        self.childProcess.daemon = True
        self.childProcess.start()
        #atexit.register(self.killQueueSubscriber)

    def killQueueSubscriber(self):
        self.childProcess.terminate()

    def getQueueSubscriber(self):
        filepath = os.path.join(self.directory, self.constants.getFilename())
        try:
            subscriber = MyZeroMQSubscriber()
            subscriber.startSubscriber(filepath)
        except zmq.error.ZMQError as error:
            monitorLog.logError("Subscriber process already running", error)
            pass
    '''
