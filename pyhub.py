import sys
import time
from extShellData import *

printStuffpc = True
printStuff = True
run = True
while run == True:

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

    if printStuff == True:
        print("Hello There!")
        print("Here are the list of avaiable projects on here!")
        print("pyclock-library, pypassgen")
        print("Type 'help' for a list of avaiable commands")
        printStuff = False
    print("Please type a command.")

    command = input()

    if command == "help":
        print("!!Every command is case sensitive!!")
        print("'source' - prints github links")
        print("'quit' or 'exit' - ends the command line")
        continue

    elif command == "source":
        print("error: links not found")

    elif command == "pyclockInit":
        pyclockInit()

    elif command == "pypassgenInit":
        passgenInit()

    elif command == "shellBasic":
        print("Python shell but different. please input a command")
        cmmd = input()
        if cmmd == "createScreen1":
            pythonBasic.screens.createScreen()
    

    elif command == "quit" or command == "exit":
        print("exited")
        time.sleep(3)
        sys.exit()

    elif command != cmdList:
        print("unknown command.")
        continue