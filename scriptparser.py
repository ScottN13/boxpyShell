from boxEngine import *
from configparser import ConfigParser
import pathlib
import os
import sys
import time
import glob

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
        for self.files in self._dir: # iterating through every file in the directory
            print(f"Combing ('{self.files}')")
            os.system("clear")
            os.system("cls")
            if self.files == name: # if we find the target file, we should read the and return the contents
                with open(name, "r", "utf-8") as file:
                    self.contents = file.read()
                    if self.contents == "":
                        print(f"Error: {file} was empty..") 
                        time.sleep(2)
                        exit(1)
                    return self.contents
        else:
            raise Exception(f"Couldn't find {name} on this device..")
            
            
    def add_command_to_main_file(self, command_name: str, script_name: str, function_name: str) -> None:
        with open(".\\boxpyshell.py", "r") as file:
            _contents = file.read()
        new_contents = f"import {script_name}\n{_contents}\nelif command == '{command_name}':\n    {function_name}({*args}, {**kwargs})" # tbh idk what this does, but it works.. I think
        with open(".\\boxpyshell.py", "w") as file:
            file.write(new_contents)
        
     
    def add_file_to_list(self, name: str) -> None:
        with open("_scripts.txt", "w") as file:
            if os.path.exists(name) and name[-3:] == ".py": # if the file exists and the file is a python file, we append the filename to "_scripts.txt"
                file.write(name) 
                print(f"Successfully added {name} to '_scripts.txt'")
            else:
                print(f"{name} is an invalid file (Maybe you forgot to add '.py' to the end?)")
                exit(1)
        
        
    def build_file(self, name: str) -> None:
        self._contents: str = self.get_script_from_user(input("Path to the Script file -> "))
        self.name: str = f"{name}.py" if name[-3:] != ".py" else name # we append the ".py" file extension if name doesn't have it
        try:
                        
            if os.path.exists("scripts"):
                with open(f".\\scripts\\{self.name}", "w") as file:
                    file.write(f"# Script for BoxPyShell\n{self._contents}")
            if not os.path.exists("scripts"):
                os.mkdir("scripts")
                with open(f".\\scripts\\{self.name}", "w") as file:
                    file.write(f"# Script for BoxPyShell\n{self._contents}")
            self.add_files_to_list(self.name)
            
        except Exception as Err:
            if type(Err) == PermissionError:
                print(f"Unable to create {self.file} due to a PermissionError") 
            else: 
                print(f"Unable to create {self.file} -> {Err}")
        
        
    def run(self) -> None: # basically just a wrapper function that brings it all together
        self.build_file(input("What do you want to name your script? -> "))
        self.add_command_to_main_file(input("Name of command? -> "), input("Name of source file? -> "), input("Name of function to be run? -> "))
        
        
if __name__ == "__main__":
    main = RemoteScriptBuilder()
    main.run()
# This is a parser for scripts that users can implement into boxpyshell
# You can make your own python script and implement it into the "scripts" folder.
# One step closer to release. 2023 might just be the year!
