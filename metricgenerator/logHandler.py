import logging
import os
import socket
import json
from common.Constants import Constants
from common.handler import Handler

log = logging.getLogger("metricgenerator")

class LogHandler:

    def __init__ (self, service, configFile):
        try:
            self.handler = Handler(service, configFile)
        except Exception:
            log.error("Cannot Instantiate Handler with configFile : " + `configFile`)
            raise Exception("Cannot Instantiate Handler with configFile : " + `configFile`)
        ''' Subscriber is now an independent process , hence following lines are commented '''
        self.commonLog = Constants.createDictCommon(service)

    '''
        Input - takes a string parameter 'msg' and an integer parameter specifying the logging level as 'severity'
        Logs the msg with the specified logging level.
    '''
    def appendLog (self, msg, severity):
        try:
            logger = self.handler.getLogHandler()
            queueHandler = self.handler.getQueueHandler()
        except Exception:
            log.error("Cannot instanstiate ZMQ handler with given context")
            raise Exception("Cannot instanstiate ZMQ handler with given context")
        try:
            with queueHandler:
                customLogDict = {}
                customLogDict.update(self.commonLog)
                customLogDict.update(msg)
                logger.log(severity,
                           json.dumps(customLogDict))
        except Exception:
            log.error("Failure to append Log: " + json.dumps(msg))
            raise Exception("Failure to append log: " + json.dumps(msg))

    def appendFailCountLog(self, name, count, severity, addOnInfoPairs = {}):
        msg = Constants.toDictCount(name, Constants.FAILCOUNT, count, severity)
        msg.update(addOnInfoPairs)
        try:
            self.appendLog(msg, severity)
        except Exception:
            log.error("Failure to append Count Log: " + json.dumps(msg))
            raise Exception("Failure to append Count log: " + json.dumps(msg))

    def appendCountLog(self, name, count, severity, addOnInfoPairs = {}):
        msg = Constants.toDictCount(name, Constants.COUNT, count, severity)
        msg.update(addOnInfoPairs)
        try:
            self.appendLog(msg, severity)
        except Exception:
            log.error("Failure append Count Log: " + json.dumps(msg))
            raise Exception("Failure to append Count log: " + json.dumps(msg))

    def appendTimeLog(self, name, runtime, severity = 20, addOnInfoPairs = {}):
        #converting the runtime to ms
        runtime = runtime*1000
        msg = Constants.toDictRuntime(name, Constants.RUNTIME, runtime, severity)
        msg.update(addOnInfoPairs)
        try:
            self.appendLog(msg, severity)
        except Exception:
            log.error("Failure to append Time Log: " + json.dumps(msg))
            raise Exception("Failure to append Time log: " + json.dumps(msg))

    '''
      list of arguments takes indices of arguments in *args assuming the each argument to be searched being json/dict.
      list of keys is the keys corresponding to an argument to be looked for.
    '''
    def appendKeysToLog(self, listOfKeys, *args):
        listOfKeys = json.loads(listOfKeys)
        customDict = {}
        try:
            for i in listOfKeys:
                if listOfKeys[i] is not []:
                    for key in listOfKeys[i]:
                        customDict = Constants.addKeyValue(key,
                                                       getattr(args[int(i)], key), customDict)
        except:
            log.error("Error while appending keys to log record :" + `listOfKeys`)
            raise Exception("Error while appending keys to log record :" + `listOfKeys`)
        return customDict
