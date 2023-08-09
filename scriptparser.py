from boxEngine import *
from configparser import ConfigParser

import os
from os.path import exists, isdir
import sys
import time

import_failed = False
try:
    from _scripts import _scripts
except Exception:
    import_failed = True
    with open("_scripts.py", "w") as file:
        file.write("")

config = ConfigParser()
config.read("config/cmds.ini")

class RemoteScriptBuilder:
    """
    Script Parser:
    
    Takes a user script and implements it into boxpyshell (if all goes well)
    All params are dealt with in the class so no need to specify them when calling the run function
    """
  
    def __init__(self):
        if exists("packages") is False:
            os.mkdir("packages")
        
        
    def get_script_from_user(self, path_name: str):
        if path_name[-3:] != ".py":
            raise Exception("Invalid File Format (Must be '.py'!)")
        
        if exists(path_name) and isdir(path_name) is False:
            with open(path_name, "r") as file:
                self.contents = file.read()
                if self.contents == "":
                    print(f"Error: Unable to open {path_name}")
                    time.sleep(3)
                    sys.exit()
                else:
                    return self.contents
        else:
            raise Exception(f"Couldn't find {path_name} on this device..")
        
     
    def add_file_to_list(self, name, path_to_package):
        name = name.split(".py", 2)
        if import_failed is True:
            _list = [name[0], path_to_package]
            contents = f"""# Package List
def _scripts():
    return {_list}
"""
        else:
            _list = _scripts()
            _list.append(name[0])
            _list.append(path_to_package)
            contents = f"""# Package List
def _scripts():
    return {_list}
"""

        with open("_scripts.py", "w") as file:
            file.write(f"{contents}")
        
        
    def build_file(self, name: str):
        self._contents = self.get_script_from_user(input("Path to the Script file -> "))
        self.name = f"{name}.py" if name[-3:] != ".py" else name
        try:
            if os.path.exists("packages") is True:
                with open(f".\\packages\\{self.name}", "w") as file:
                    file.write(f"'Package for BoxPyShell'\n{self._contents}")
                self.path_to_package = os.path.abspath(f".\\packages\\{name}.py")

            self.add_file_to_list(self.name, self.path_to_package)
        except Exception as Err:
            print(f"Unable to create {self.file} due to a PermissionError") if type(Err) == PermissionError else print(f"Unable to create {self.file} -> {Err}")
        
        
    def run(self):
        self.build_file(input("What do you want to name your script? -> "))
        
        
if __name__ == "__main__":
    main = RemoteScriptBuilder()
    main.run()
# This is a parser for scripts that users can implement into boxpyshell
# You can make your own python script and implement it into the "scripts" folder.
# One step closer to release. 2023 might just be the year!
