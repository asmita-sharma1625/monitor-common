from metricgenerator.common import configWriter, configReader
import os
import sys
import socket

arg_len = len(sys.argv)
i = 1

if arg_len <= 2:
  raise SystemExit("Invalid Arguments")
if arg_len > 2:
  CONFIGFILE = sys.argv[i]
  i += 1
  SECTION = sys.argv[i]
  i += 1

while i < arg_len:
  option = sys.argv[i]
  i += 1
  if i == arg_len:
    raise SystemExit("Invalid Arguments")
  val = sys.argv[i]
  i += 1
  if option == "--service":
    configWriter.CreateConfigFile(CONFIGFILE, SECTION, "Service", val)
  if option == "--logdir":
    configWriter.CreateConfigFile(CONFIGFILE, SECTION, "LogDir", val)
  if option == "--filename":
    configWriter.CreateConfigFile(CONFIGFILE, SECTION, "Filename", val)
  if option == "--socket":
    configWriter.CreateConfigFile(CONFIGFILE, SECTION, "Socket", val)
  if option == "--bucket":
    configWriter.CreateConfigFile(CONFIGFILE, SECTION, "Bucket", val)

HOSTNAME = socket.gethostname()
configWriter.CreateConfigFile(CONFIGFILE, SECTION, "Hostname", HOSTNAME)
configReader.ConfigReader.setConfig(CONFIGFILE)

