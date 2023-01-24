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
    exit("Error! Config file missing!")


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
        print("Hello There!\n# Reminder!! Every command is CaSe SeNsItIvE\nType 'help' for a list of avaiable commands")     
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
    
    elif command in ("build", "run"):
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
