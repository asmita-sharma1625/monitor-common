from logger.consumer import Consumer
from logger.common.Constants import Constants
from logger.common import configWriter
from logger.common.configReader import ConfigReader
import pdb


configWriter.CreateConfigFile("config.cfg", "Constants", "LogDir", ".")
ConfigReader.setConfig("config.cfg")

pdb.set_trace()
consumer = Consumer(Constants.getLogDir(), deleterotatedfiles = False, logpattern = "metric.*\.log", target_path = "./consumer/")
consumer.consume() 
