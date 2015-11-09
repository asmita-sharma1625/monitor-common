from logger import Logger

logger = None

def setLogger(service, configFile):
    global logger
    logger  = Logger(service, configFile)

#TODO :  make changes for logIfFAil 
def LogIfFail(name, expectedReturn, counter, severity = None):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            return logger.logIfFail(name, expectedReturn, counter, function, severity, *args, **kwargs)
        return wrapper
    return real_decorator

def ReportLatency(name, severity = None):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
	   global logger
	   print "*****logger object *****" + `logger`
           return logger.reportLatency(name, function, severity, *args, **kwargs)
        return wrapper
    return real_decorator

