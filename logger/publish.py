from logger import Logger

logger = None

def setLogger(service):
    global logger
    logger  = Logger(service)

def LogIfFail(name, metricType, expectedReturn, counter):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            logger.logIfFail(name, metricType, expectedReturn, counter, function, *args, **kwargs)
        return wrapper
    return real_decorator

def ReportLatency(name, metricType):
    def real_decorator(function):
        def wrapper(*args, **kwargs):
            logger.reportLatency(name, metricType, function, *args, **kwargs)
        return wrapper
    return real_decorator

