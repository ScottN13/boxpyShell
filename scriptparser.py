from boxEngine import *
from configparser import ConfigParser
import pathlib
import os
import sys
import time

config = ConfigParser()
config.read("config/cmds.ini")

class RemoteScriptBuilder:
    """
    Script Parser:
    
    Takes a user script and implements it into boxpyshell (if all goes well)
    All params are dealt with in the class so no need to specify them when calling the run function
    """
  
    def __init__(self) -> None:
        ...
        
        
    def get_script_from_user(self, name: str) -> str:
        if name[-3:] != ".py":
            raise Exception("Invalid File Format (Must be '.py'!)")
        self._dir = glob.glob(fr"{pathlib.Path.home().drive}\\**\\{name}")
        for self.files in self._dir:
            print(f"Combing ('{self.files}')")
            os.system("clear")
            os.system("cls")
            if self.files == name:
                with open(name, "r", "utf-8") as file:
                    self.contents = file.read()
                    if self.contents == "":
                        print(f"Error: Unable to open {name}")
                        time.sleep(3)
                        sys.exit()
                    return self.contents
        else:
            raise Exception(f"Couldn't find {name} on this device..")
        
     
    def add_file_to_list(self, name) -> None:
        with open("_scripts.txt", "w") as file:
            if os.path.exists(name) is True and name[-3:] == ".py":
                file.write(f"{name}")
                print(f"Successfully added {name} to '_scripts.txt'")
            else:
                print(f"{name} is an invalid file (Maybe you forgot to add '.py' to the end?)")
        
        
    def build_file(self, name: str) -> None:
        self._contents = self.get_script_from_user(input("Path to the Script file -> "))
        self.name = f"{name}.py" if name[-3:] != ".py" else name
        try:
            if os.path.exists("scripts") is True:
                with open(f".\\scripts\\{self.name}", "w") as file:
                    file.write(f"'Script for BoxPyShell'\n{self._contents}")
            if os.path.exists("scripts") is False:
                os.mkdir("scripts")
                with open(f".\\scripts\\{self.name}", "w") as file:
                    file.write(f"'Script for BoxPyShell'\n{self._contents}")
            self.add_files_to_list(self.name)
        except Exception as Err:
            print(f"Unable to create {self.file} due to a PermissionError") if type(Err) == PermissionError else print(f"Unable to create {self.file} -> {Err}")
        
        
    def run(self) -> None:
        self.build_file(input("What do you wamt to name your script? -> "))
        
        
if __name__ == "__main__":
    main = RemoteScriptBuilder()
    main.run()
# This is a parser for scripts that users can implement into boxpyshell
# You can make your own python script and implement it into the "scripts" folder.
# One step closer to release. 2023 might just be the year!
