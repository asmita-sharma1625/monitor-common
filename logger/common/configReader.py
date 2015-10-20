import ConfigParser

CONFIGFILE = "/home/asmi/monitor-common/config.cfg"
config = ConfigParser.RawConfigParser()
config.read(CONFIGFILE)

def getValue(section, key):
  return config.get(section, key) 

