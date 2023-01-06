from extShellData import *
from configparser import ConfigParser

config = ConfigParser()
config.read("config/cmds.ini")

# This is a parser for scripts that users can implement into boxpyshell
# You can make your own python script and implement it into the "scripts" folder.
# One step closer to release. 2023 might just be the year!