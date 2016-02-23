from metricgenerator.logger import Logger

class Publish:

    def __init__(self, service, configFile = None):
        self.logger = Logger(service, configFile)

    #TODO :  make changes for logIfFAil
    def LogIfFail(self, name, expectedReturn, counter, severity = 20):
        def real_decorator(function):
            def wrapper(*args, **kwargs):
                return self.logger.logIfFail(name, expectedReturn, counter, function, severity, *args, **kwargs)
            return wrapper
        return real_decorator

    def ReportLatency(self, name, severity = 20, listOfKeys = []):
        def real_decorator(function):
            def wrapper(*args, **kwargs):
                return self.logger.reportLatency(name, function, severity,\
                                       listOfKeys, *args, **kwargs)
            return wrapper
        return real_decorator

