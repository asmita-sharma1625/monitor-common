import logging
import os
import socket
import json
from common.Constants import Constants
from common.handler import Handler
from common.monitorLog import monitorLog

class LogHandler:

    def __init__ (self, service, configFile):
        try:
            self.handler = Handler(service, configFile)
        except Exception as error:
            monitorLog.logError("Cannot Instantiate Handler with configFile : " + configFile, `error`)
            raise Exception("Cannot Instantiate Handler with configFile : " + configFile)
        ''' Subscriber is now an independent process , hence following lines are commented '''
        # start queue subscriber for logging
        # self.handler.startQueueSubscriber()
        #self.commonLog = Constants.toStringCommon(service)
        self.commonLog = Constants.createDictCommon(service)

    '''
        Input - takes a string parameter 'msg' and an integer parameter specifying the logging level as 'severity'
        Logs the msg with the specified logging level.
    '''
    def appendLog (self, msg, severity):
        try:
            logger = self.handler.getLogHandler()
            queueHandler = self.handler.getQueueHandler()
        except Exception as error:
            monitorLog.logError("Cannot instanstiate ZMQ handler with given context", `error`)
            raise Exception("Cannot instanstiate ZMQ handler with given context")
        try:
            with queueHandler:
                customLogDict = {}
                customLogDict.update(self.commonLog)
                customLogDict.update(msg)
                logger.log(severity,
                           json.dumps(customLogDict))
        except Exception as error:
            monitorLog.logError("Failure to append Log: " + json.dumps(msg), `error`)
            raise Exception("Failure to append log: " + json.dumps(msg))

    def appendFailCountLog(self, name, count, severity):
        msg = Constants.toStringCount(name, Constants.FAILCOUNT, count, severity)
        try:
            self.appendLog(msg, severity)
        except Exception as error:
            monitorLog.logError("Failure to append Count Log: " + json.dumps(msg), `error`)
            raise Exception("Failure to append Count log: " + json.dumps(msg))

    def appendCountLog(self, name, count, severity):
        msg = Constants.toStringCount(name, Constants.COUNT, count, severity)
        try:
            self.appendLog(msg, severity)
        except Exception as error:
            monitorLog.logError("Failure append Count Log: " + json.dumps(msg), `error`)
            raise Exception("Failure to append Count log: " + json.dumps(msg))

    def appendTimeLog(self, name, runtime, severity):
        #converting the runtime to ms
        runtime = runtime*1000
        msg = Constants.toDictRuntime(name, Constants.RUNTIME, runtime, severity)
        #print (json.dumps(msg))
        try:
            #print (msg)
            self.appendLog(msg, severity)
        except Exception as error:
            monitorLog.logError("Failure to append Count Log: " + json.dumps(msg), `error`)
            raise Exception("Failure to append Count log: " + json.dumps(msg))
