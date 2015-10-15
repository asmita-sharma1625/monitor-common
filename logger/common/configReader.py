import ConfigParser
import sys

assert len(sys.argv) == 4

filepath = sys.argv[1]
section = sys.argv[2]
key = sys.argv[3]

config = ConfigParser.RawConfigParser()
config.read(filepath)

value = config.get(section, key)
print value

