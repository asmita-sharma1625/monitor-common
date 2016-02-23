import os
import sys
import logging
from logging import handlers

logger = logging.getLogger("metricgenerator")
logger.setLevel(logging.INFO)
LOG_FORMAT = "%(asctime)s - %(name)s - %(pathname)s - %(funcName)s -%(thread)d - %(levelname)s - %(message)s"
LOGFILE = "/var/log/metricgenerator/metricgenerator"
''' configure logger'''
formatter = logging.Formatter(LOG_FORMAT)
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(formatter)
logger.addHandler(ch)
fh = logging.handlers.RotatingFileHandler(LOGFILE, maxBytes=(1048576*5), backupCount=7)
fh.setFormatter(formatter)
logger.addHandler(fh)
