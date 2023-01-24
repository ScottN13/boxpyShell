from extShellData import *
from configparser import ConfigParser
import pathlib
import os
import sys
import time

config = ConfigParser()
config.read("config/cmds.ini")

class RemoteScriptBuilder:
  
    def __init__(self):
        ...
        
    def get_script_from_user(self, path):
        if os.path.exists(path) is True:
            with open(path, "r", "utf-8") as file:
                self.contents = file.read()
                if self.contents == "":
                    self.file = os.path.split(path) # Getting file from path for error message
                    print(f"Error: Unable to open {self.file[1]}")
                    time.sleep(3)
                    sys.exit()
             return self.contents
        sys.exit(f"The path provided doesn't exist on this machine..") if os.path.exists(path) is False else None # spaghetti (change later)
        
    def build(self):
        self._contents = self.get_script_from_user(input("Path to the Script file -> "))
        with open("file0.py", "w") as file:
            file.write(self._contents)
        try:
            os.system("python file0.py")
        except PermissionError:
            try:
                subprocess.call(["python file0.py"])
            except PermissionError:
                print("Unable to run program due to a PermissionError")
        os.remove("file0.py")
        
if __name__ == "__main__":
    main = RemoteScriptBuilder()
    main.build()
# This is a parser for scripts that users can implement into boxpyshell
# You can make your own python script and implement it into the "scripts" folder.
# One step closer to release. 2023 might just be the year!
