from metricgenerator.logger import Logger

logger = None

def setLogger(service, configFile):
    global logger
    logger  = Logger(service, configFile)

#TODO :  make changes for logIfFAil
def LogIfFail(name, expectedReturn, counter, severity = 20):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            return logger.logIfFail(name, expectedReturn, counter, function, severity, *args, **kwargs)
        return wrapper
    return real_decorator

def ReportLatency(name, severity = 20, listOfKeys = []):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
           return logger.reportLatency(name, function, severity,\
                                       listOfKeys, *args, **kwargs)
        return wrapper
    return real_decorator

