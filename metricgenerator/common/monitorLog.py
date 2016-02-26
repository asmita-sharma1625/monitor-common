import os
import sys, stat
import logging
from logging import handlers

def configure_logging(logformat, logfile):
    logger = logging.getLogger("metricgenerator")
    open(logfile, "a").close()
    #os.chmod(logfile, 0666)
    logger.setLevel(logging.DEBUG)
    ''' configure logger'''
    formatter = logging.Formatter(logformat)
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fh = logging.handlers.RotatingFileHandler(logfile, maxBytes=(1048576*5), backupCount=7)
    fh.setFormatter(formatter)
    logger.addHandler(fh)
