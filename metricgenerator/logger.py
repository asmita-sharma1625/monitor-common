import time
import threading
import logging
from logHandler import LogHandler
from common.exceptions import IncorrectConfigException, LoggingException

log = logging.getLogger("metricgenerator")

class Logger:
    '''
    #beyond these, email will be triggered.
    threshold_failure = 20
    threshold_latency = 20
    threshold_count = 20
    '''
    '''
        It :
            - Creates LogHandler instance to write metrics to log file.
            - Creates threading.local() instance to create thread specific variables.
    '''
    def __init__ (self, service, configFile = None):
        try:
            self.logHandler = LogHandler(service, configFile)
            log.debug("logger instantiated")
        except Exception:
            log.error("Cannot Instantiate Logger with configFile : " + `configFile`)
            #raise IncorrectConfigException("Cannot Instantiate Logger with configFile : " + `configFile`)
            pass
        self.threadLocal = threading.local()
        self.counter = 0;

    '''
        If the given action is failed, then it will log the failure count uptil now.
        It will also return the updated counter value.
    '''
    '''
    def logIfFail (self, name, expectedReturn, counter, action, severity = 20, *args, **kwargs):
        count = self.reportCountNE(expectedReturn, counter, action, *args, **kwargs)
        if count > 0:
            try:
                #print "logging failure"
                self.logHandler.appendFailCountLog(name, count, severity)
            except Exception:
                log.error("Failed to append log for metric: " + name)
                raise LoggingException("Failed to append log for metric: " + name)
        return count
    '''

    def logFailure (self, name, counter = 1, severity = 20, addOnInfoPairs = {}):
        if counter > 0:
            try:
                '''
                if counter >= Logger.threshold_failure:
                    self.logHandler.appendFailCountLog(name, counter,  50)
                '''
                self.logHandler.appendFailCountLog(name, counter, severity, addOnInfoPairs)
                #print "logging failure"
            except Exception:
                log.error("Failed to append log for metric: " + name)
                #raise LoggingException("Failed to append log for metric: " + name)
            return 1
        return 0

    def logCount (self, name, counter = 1, severity = 20, addOnInfoPairs = {}):
        if counter > 0:
            try:
                #print "inside logCount method for metric name - ", name
                '''
                if counter >= Logger.threshold_count:
                    self.logHandler.appendCountLog(name, counter,  50)
                '''
                self.logHandler.appendCountLog(name, counter, severity, addOnInfoPairs)
            except Exception:
                log.error("Failed to append log for metric: " + name)
                #raise LoggingException("Failed to append log for metric: " + name)
            return 1
        return 0


    '''
        Report the incremented counter if the action has failed to pass the expectation.

    '''
    def reportCountEqual(self, expectedReturn, counter, action, *args, **kwargs):
        try:
            actualReturn = action(*args, **kwargs)
        except:
            return counter + 1
        if actualReturn == expectedReturn:
            return counter + 1
        return counter

    '''
        Report the incremented counter if the action has passed the expectation.
    '''
    def reportCountNE(self, expectedReturn, counter, action, *args, **kwargs):
        try:
            actualReturn = action(*args, **kwargs)
        except:
            return counter + 1
        if actualReturn == expectedReturn:
            return counter
        return counter + 1

    '''
        Starts the thread local timer.
    '''
    def startTime (self):
        #using thread local storage for start time
        self.threadLocal.startTime = time.time()

    '''
        Stops the thread local timer and logs the execution time.
    '''
    def reportTime (self, name, severity = 20, addOnInfoPairs = {}):
        endTime = time.time()
        runTime = endTime - self.threadLocal.startTime
        try:
            '''
            if runTime >= Logger.threshold_latency:
                self.logHandler.appendTimeLog(name, runTime, 50)
            '''
            self.logHandler.appendTimeLog(name, runTime, severity, addOnInfoPairs)
        except Exception:
            log.error("Failed to append log for metric: " + name)
            #raise LoggingException("Failed to append log for metric: " + name)

    '''
        Logs the execution time of the given action and returns the value of action.
    '''
    def reportLatency (self, name, action, severity = 20,listOfKeys = '{}', *args, **kwargs):
        keyValuePairs = {}
        try:
            if listOfKeys is not '{}':
                keyValuePairs = self.logHandler.appendKeysToLog(listOfKeys, *args)
        except:
            log.error("Error while appending keys to log record :" + `listOfKeys`)
            pass
        self.startTime()
        try:
            actualReturn = action(*args, **kwargs)
        except Exception:
            log.error("Failed Action " + `action`)
            #raise Exception("Failed Action :" + `action`)
        self.reportTime(name, severity, keyValuePairs)
        return actualReturn
