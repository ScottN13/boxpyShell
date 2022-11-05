from configparser import ConfigParser
import sys
import time
from extShellData import *
from nbdpy import *

printStuffpc = True
printStuff = True
run = True
config = ConfigParser()
config.read("mainConfig.ini")

passPrint = "Please input password (Press enter if none was added): "

try:
    config_data1 = str(config["MAIN"]["debug"])
    if config_data1 == "false":
        animlib.loadingAnim("load",5)
    elif config_data1 == "true":
        print("debug mode = true")

except:
    exit("Error! Config file or an element is missing!")


try:
    ConfigDebugCheck = str(config["MAIN"]["skipUsers"])
    if ConfigDebugCheck == "false":
        user = input("Please login (Admin or User1): ")
        if user == "ADMIN":
            password = input(passPrint)
            if password != "123456":
                print("Wrong Password! Exiting...")
                exit(0)

            try:
                config_data2 = config[user]
            
            except:
                print("User Not found! Exiting...")
                exit(0)

    elif ConfigDebugCheck == "true":
        print("skipping user selection")

except:
    exit("Error! Config file or an element is missing!")


while run == True:

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

    user = input("Please login (Admin or User1): ")


    if printStuff == True:
        print("Hello There!")
        print("# Reminder!! Every command is CaSe SeNsItIvE")
        print("Type 'help' for a list of avaiable commands")
        printStuff = False
    print("Please type a command.")


    command = input()

    if command == "help":
        print("Select which type of help to display: basic, ext1, ext2")
        typeHelp = input()

        if typeHelp == "basic":
            file_path = 'data/help.txt'
            with open(file_path) as file:
                print(file.read())

        elif typeHelp == "ext1":
            file_path = 'data/hpc.txt'
            with open(file_path) as file:
                print(file.read())

        elif typeHelp == "ext2":
            file_path = 'data/hpg.txt'
            with open(file_path) as file:
                print(file.read())

        continue

    elif command == "readEX":
        file_pathEX = 'data/helloworld.txt'
        print('This is just a demonstration of the reading ability of boxpyshell')
        print("Please wait...r")
        animlib.loadingAnim("load",5)
        spamClear()
        with open(file_pathEX) as file:
            print(file.read())           

    elif command == "source":
        print("error: links not found")

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

    elif command == "quit" or command == "exit":
        animlib.loadingAnim("exit",5)
        print("terminated main task. exit")
        sys.exit()

    elif command != cmdList:
        print("unknown command.")
        continue
