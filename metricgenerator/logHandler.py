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
        print "msg : ", msg
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
            monitorLog.logError("Failure to append Log: " + msg, `error`)
            raise Exception("Failure to append log: " + msg)

    def appendFailCountLog(self, name, count, severity):
        msg = Constants.toStringCount(name, Constants.FAILCOUNT, count, severity)
        try:
            self.appendLog(msg, severity)
        except Exception as error:
            monitorLog.logError("Failure to append Count Log: " + msg, `error`)
            raise Exception("Failure to append Count log: " + msg)

    def appendCountLog(self, name, count, severity):
        msg = Constants.toStringCount(name, Constants.COUNT, count, severity)
        try:
            self.appendLog(msg, severity)
        except Exception as error:
            monitorLog.logError("Failure append Count Log: " + msg, `error`)
            raise Exception("Failure to append Count log: " + msg)

    def appendTimeLog(self, name, runtime, severity, addOnInfoPairs = {}):
        print "add ons : ", addOnInfoPairs
        msg = Constants.toDictRuntime(name, Constants.RUNTIME, runtime, severity)
        msg.update(addOnInfoPairs)
        #print (json.dumps(msg))
        try:
            #print (msg)
            self.appendLog(msg, severity)
        except Exception as error:
            monitorLog.logError("Failure to append Count Log: " + msg, `error`)
            raise Exception("Failure to append Count log: " + msg)
    '''
      list of arguments takes indices of arguments in *args assuming the each argument to be searched being json/dict.
      list of keys is the keys corresponding to an argument to be looked for. 
    '''
    def appendKeysToLog(self, listOfArguments, listOfKeys, *args):
        customDict = {}
        for i in range(0,len(listOfArguments)):
            if listOfKeys[i] is not []:
                for key in listOfKeys[i]:
                    customDict = Constants.addKeyValue(key, args[listOfArguments[i]][key], customDict)
        return customDict 

