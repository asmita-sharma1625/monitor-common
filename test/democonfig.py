from logger.common import configWriter, configReader
import os 

class demoConfig:

  socket = 5578
  section = "Constants"

  def __init__(self, cfgfile):
    self.cfgfile = cfgfile

  def setConfig(self):
    demoConfig.socket = demoConfig.socket + 1
    print "----cwd-----", os.path.abspath(os.curdir)
    configWriter.CreateConfigFile(self.cfgfile, self.section, "Socket", "tcp://127.0.0.1:"+`demoConfig.socket`)
    configWriter.CreateConfigFile(self.cfgfile, self.section, "LogDir", "./logs")
    configWriter.CreateConfigFile(self.cfgfile, self.section, "Filename", "metric.log")
    configReader.ConfigReader.setConfig(self.cfgfile)
    
