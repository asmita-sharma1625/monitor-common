from logger.common import configWriter, configReader

class demoConfig:

  socket = 5578
  cfgfile = "./Config.cfg"
  section = "Constants"

  def __init__(self):
    pass

  def setConfig(self):
    demoConfig.socket = demoConfig.socket + 1
    configWriter.CreateConfigFile(self.cfgfile, self.section, "Socket", "tcp://127.0.0.1:"+`demoConfig.socket`)
    configWriter.CreateConfigFile(self.cfgfile, self.section, "LogDir", "./logs")
    configWriter.CreateConfigFile(self.cfgfile, self.section, "Filename", "metric.log")
    configReader.ConfigReader.setConfig(self.cfgfile)
    return self.cfgfile
