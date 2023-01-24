from configparser import ConfigParser
import sys
import time
from extShellData import *
from nbdpy import *
# from userLogon import *

printStuffpc = True
printStuff = True
run = True
cmdTagSuffix = ""
OSNAME = 
cmdTagPrefix = f"boxpyshell@{OSNAME} $~: "
cmdTagFull = str(cmdTagSuffix + cmdTagPrefix)
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

    if printStuff == True:
        print("Hello There!, ","Type 'help' for a list of avaiable commands")
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
        file_pathEX = 'data/helloworld.txt'
        print('This is just a demonstration of the reading ability of boxpyshell')
        print("Please wait...")
        animlib.loadingAnim("load",2)
        spamClear()
        with open(file_pathEX) as file:
            print(file.read())           

    elif command == "source":
        file_pathSource = "data/source.txt"
        with open(file_pathSource) as file:
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


    #elif command == "createFile":
     #   os.

    elif command in ("quit", "exit"):
        animlib.loadingAnim("exit", 5)
        print("terminated main task. exit")
        sys.exit()

    elif command != cmdList:
        print("unknown command.")
        continue
