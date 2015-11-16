from metricgenerator.consumer import Consumer
from metricgenerator.common.Constants import Constants
from metricgenerator.common import configWriter
from metricgenerator.common.configReader import ConfigReader
import pdb


configWriter.CreateConfigFile("config.cfg", "Constants", "LogDir", ".")
ConfigReader.setConfig("config.cfg")

pdb.set_trace()
consumer = Consumer(Constants.getLogDir(), deleterotatedfiles = False, logpattern = "metric.*\.log", target_path = "./consumer/")
consumer.consume() 
