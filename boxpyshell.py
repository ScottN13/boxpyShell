from configparser import ConfigParser
from scriptparser import RemoteScriptBuilder
import sys
import time
import os
from extShellData import *
from nbdpy import *
# from userLogon import *

printStuffPc, printStuff, run = True, True, True
OSNAME = os.getlogin()
config = ConfigParser()
config.read("config/main.ini")

try:
    config_data1 = str(config["DEBUG"]["noloading"])
    print(config_data1)
    if config_data1 == "false":
        animlib.loadingAnim("load",5)
    elif config_data1 == "true":
        print("skipped animlib")
        debugMode = True

except Exception as Err:
    exit(f"Error! Config file or an element is missing! -> {Err}")

while run is True:

    """
    def pyclockInit():
       # from pyclock import *
        if printStuffpc == True:
            print("init pyclock-library")
            print("hpc for a list of  commands")
            print("!!!WARRNINGG!!! This version of pyclock is 0.4 experimental and has some bugs with the events class!")
            print("Learn more on the pull request i made on github. You can get the links by putting 'source' on the main menu terminal")
            printStuffpc = False
        print("please type a command.")
     
    def passgenInit():
        #from passgen import *
        print("init pypassgen")
        print("hpg for a list of commands")

    """ 

    if printStuff is True:
        print("Hello There!, Type 'help' for a list of avaiable commands")
        printStuff = False
    print("Please type a command.")


    command = input(f"boxpyshell@{OSNAME} $~: ")

    if command == "help":
        print("Select which type of help to display: basic, ext1, ext2")
        typeHelp = input(" -> ")

        if typeHelp == "basic":
            with open('data/help.txt') as file:
                print(file.read())

        elif typeHelp == "ext1":
            with open('data/hpc.txt') as file:
                print(file.read())

        elif typeHelp == "ext2":
            with open('data/hpg.txt') as file:
                print(file.read())

        continue

    elif command == "readEX":
        print('This is just a demonstration of the reading ability of boxpyshell')
        print("Please wait...")
        animlib.loadingAnim("load", 2)
        spamClear()
        with open('data/helloworld.txt') as file:
            print(file.read())           

    elif command == "source":
        with open("data/source.txt") as file:
            print(file.read())


    elif command == "screenCreate":
        print("Please input a command")
        cmmd = input()
        if cmmd == "createScreen1":
            pythonBasic.screens.createScreen()
            
    elif command == "addScript":
        main = RemoteScriptBuilder()
        main.run()

    elif command == "echo":
        txtE = input("Type something to echo: ")
        for i in range(5):
            print("")
        extFunc.funct.echo(txtE)
        ##########################
        #You could also do:
        #
        #import re as regex
        #
        #find_echo_string = regex.search('"', command)
        #index_of_string = find_echo_string.span()
        #echo_string = command[index_of_string[1]:-1:1] # -> Slicing from the start of the string to the end of the string to get the contents
        #
        #print(echo_string)
        #
        #So if my input was -> echo "Hello World!"
        #it would return with just -> Hello World!
        #
        #this just makes the command more immediate

        # ok, but i have no experience in regex -es -- valko
        
    elif command in ("?", "!"): #Command Flags for executing code
        try:
            exec(command[1:]) # Splitting the command flag from the string so we can run it
        except Exception as Err:
            print(f"Couldn't run code (Error Received) -> {Err}")
    
    elif command in ("build", "run"): # command should be structured like (build {filename}.py >> .exe) or (run {filename}.py)
        command = command.split(" ", 4)
        try:
            if os.path.exists(command[1]) and ".py" in command[1]:
                if command[2] in (">>", "->") and command[3] == ".exe":
                    with open("file0.py", "w") as file:
                        file.write(f"""import subprocess
try:
    import PyInstaller.__main__
except ModuleNotFoundError:
    subprocess.call(['python', '-m', 'pip', 'install', 'pyinstaller'])
PyInstaller.__main__.run(['{command[1]}','--onefile'])""")
                    try:
                        os.system("python file0.py")
                        os.system("py file0.py")
                        print(f"Successfully built {command[1]} to .exe")
                    except PermissionError:
                        print("PermissionError: Couldn't run file0.py")
                if command[2] == "" and command[3] == "":
                    os.system(f"python {command[1]}")
                    os.system(f"python {command[1]}")
        except IndexError:
            print("Invalid params for build command")
        command = " ".join(command, 4)

    elif command == "clearscreen":
        spamClear()
    
    elif command == "shellVer":
        extFunc.funct.shellVer()
        
    elif command == "MathAdd":
        extFunc.math.add()

    elif command == "MathSubt":
        extFunc.math.subtract()
    
    elif command == "helloMe":
        extFunc.fun.helloUser()

    elif command == "8Ball":
        extFunc.fun.eightBall()

    elif command == "YesOrNo":
        extFunc.fun.ynGame()

    elif command == "nbdpy":
        nbDisplay.startDisplay()

    elif command == "MegaExit":
        sys.exit("M E G A E X I T")

    # "createFile" is bugged: IndexError: list index is out of range: file = command[1]
    elif command == "createFile":
        command = command.split(" ", 2)
        file = command[1]
        file_extension = ".txt" if file[-5:] not in (".txt", ".py", ".c", ".rc", ".java") else ""
        with open(f"{file}{file_extension}", "w") as file:
            file.write("") # Writing nothing to the file so we can just create an empty file
        command = " ".join(command, 2)

    elif command in ("quit", "exit"):
        animlib.loadingAnim("exit", 5)
        print("terminated main task. exit")
        sys.exit()

    elif command not in cmdList:
        print(f"{command} is not a valid command!")
        continue
