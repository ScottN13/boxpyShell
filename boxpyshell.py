from configparser import ConfigParser
import sys
import time
import os
from extShellData import *
from nbdpy import *
# from userLogon import *

printStuffPc, printStuff, run = True, True, True
OSNAME = os.getlogin()
cmdTagFull = f"boxpyshell@{OSNAME} $~: "
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


    command = input(cmdTagFull)

    if command == "help":
        print("Select which type of help to display: basic, ext1, ext2")
        typeHelp = input(" -> ").lowercase()

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
        animlib.loadingAnim("load",2)
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

    elif command == "echo":
        print("Please type something to echo.")
        txtE = input()
        for i in range(5):
            print("")
        extFunc.funct.echo(txtE)
        ##########################
        #You could also do:
        #
        #import re as regex
        #
        #find_echo_string = regex.search('"', _string)
        #index_of_string = find_contents.span()
        #echo_string = _string[index_of_string[1]:-1:1] -> Slicing from the start of the string to the end of the string to get the contents
        #
        #print(echo_string)
        #
        #So if my input was -> echo "Hello World!"
        #it would return with just -> Hello World!
        #
        #this just makes the command more immediate
        
    elif command in ("?", "!"): #Command Flags for executing code
        try:
            exec(command[1:]) # Splitting the command flag from the string so we can run it
        except Exception as Err:
            print(f"Couldn't run code (Error Received) -> {Err}")

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


    # elif command == "createUser":


    elif command == "createFile":
        command = command.split(" ", 4)
        with open(command[1], "w") as file: # Here command[1] is the filename
            file.write("")
        print(f"Successfully created {command[1]}!")
        command = " ".join(command, 4)

    elif command in ("quit", "exit"):
        animlib.loadingAnim("exit", 5)
        print("terminated main task. exit")
        sys.exit()

    elif command != cmdList:
        print("unknown command.")
        continue
