import os
import logging
from metricgenerator.common.Constants import Constants
from logbook.compat import RedirectLoggingHandler
from metricgenerator.common.zeroMQHandler import MyZeroMQHandler
from metricgenerator.common.configReader import ConfigReader
import zmq

log = logging.getLogger("metricgenerator")

class Handler:

    childProcess = None

    def __init__(self, service, configFile):
        try:
            self.constants = Constants(configFile)
            self.directory = self.constants.getLogDir()
        except Exception:
            log.error("Could not retrieve logging directory from config file :" + `configFile`)
            raise Exception("Could not retrieve logging directory from config file :" + `configFile`)
        if not os.path.exists(self.directory):
                os.makedirs(self.directory)
        self.service = service
        self.logger = logging.getLogger(self.service)
        self.logger.propagate = False
        self.logger.setLevel(logging.INFO)
        if not len(self.logger.handlers):
            self.logger.addHandler(RedirectLoggingHandler())
        self.socket = self.constants.getSocket()

    def getLogHandler(self):
        logger = logging.getLogger(self.service)
        #print "Handlers:", logger.handlers()
        return logger


    def getQueueHandler(self):
        context = zmq.Context()
        return MyZeroMQHandler(self.socket, context).getZeroMQHandler()
