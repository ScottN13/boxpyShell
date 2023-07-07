from configparser import ConfigParser
from scriptparser import RemoteScriptBuilder
import sys
import time
import os
from boxEngine import *
from rich.console import Console
from rich.progress import track
from userLogon import logins

console = Console()
printStuffPc, printStuff, run = True, True, True
OSNAME = os.getlogin()
config = ConfigParser(comment_prefixes="#", delimiters="=")
config.read("config/main.ini")

# check if debug mode is on:
try:
    debug_check = str(config["DEBUG"]["isActive"])
    if debug_check == "false":
        debugMode = False
    elif debug_check == "true":
        console.print(f"["+"[bold][bright_yellow] WARN [/]"+"] Debug mode is on!")
        debugMode = True    

except Exception as Err:
    boxEngine.error.ConfigFatal(Err)

# check if the config for the animation lib has changed.
try:
    config_data1 = str(config["DEBUG"]["noloading"])
    # print(config_data1) -> THIS WAS WHAT PRINTED TRUE IN THE TERMINAL!!!
    if config_data1 == "false":
        animlib.loadingAnim("load",5)
    elif config_data1 == "true":
        console.print(f"["+"[bold][bright_green] OK [/]"+"]"+"[italic][bold][bright_red] DEBUG:[/]"+" loading animation skipped!")

except Exception as Err:
    boxEngine.error.ConfigFatal(Err)

logins.doLogin()

while run is True:
    
    if printStuff is True:
        warn("This version of boxpyshell is still in beta! There might be new releases on github!")
        print("Hello There!, Type 'help' for a list of avaiable commands")
        printStuff = False
        print("Please type a command.")


    command = console.input(f"[bold][bright_yellow]boxpyshell[/][bright_magenta]@[/][bright_green]{OSNAME}$~:[/] ")

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
        boxEngine.spamClear()
        with open('data/helloworld.txt') as file:
            print(file.read())           

    elif command == "source":
        with open("data/source.txt") as file:
            print(file.read())

    elif command == "cvar":
        boxEngine.cvar()

    elif command == "vars":
        boxEngine.vars()

    elif command == "rmdir":
        path = input("Path to remove directory: ")
        boxEngine.rmdir(path)
    
    elif command == "mkdir":
        name = input("Give a name for the new directory: ")
        if name == None or name == "":
            error("You cannot choose an empty name.")
        else:
            boxEngine.mkdir(name)

    elif command == "config":
        warn("You are changing the main.ini configuartion file. Please be warned that any typo can break boxpyshell!")
        uInput = console.input("[bold]What would block you like to change?")
        uIBlocks = ["main","debug","ext","external","m","d","e"] # List of commands, full (external), inital letters (e), shortened (ext)

        if uInput != uIBlocks: # spell check
            error(f"No such thing as {uInput}! Run the command again.")

        elif uInput == "main" or uInput == "m": # edit main
            boxEngine.error.NotImplement()

        elif uInput == "ext" or uInput == "external" or uInput == "e": # edit ext
            boxEngine.error.NotImplement()

        elif uInput == "debug" or uInput == "d":
            boxEngine.error.NotImplement()

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
        boxEngine.funct.echo(txtE)
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
        
    if command[:1] in ("?", "!"): #Command Flags for executing code
        try:
            exec(f"{command[1:]}") # Splitting the command flag from the string so we can run it
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

    elif command == "clearscreen" or command == "clear":
        boxEngine.spamClear()
    
    elif command == "shellVer":
        boxEngine.extFunc.funct.shellVer()
        
    elif command == "MathAdd":
        boxEngine.extFunc.math.add()

    elif command == "MathSubt":
        boxEngine.extFunc.math.subtract()
    
    elif command == "helloMe":
        boxEngine.extFunc.fun.helloUser()

    elif command == "8Ball":
        boxEngine.extFunc.fun.eightBall()

    elif command == "YesOrNo":
        boxEngine.extFunc.fun.ynGame()
        
    elif command == "me":
        sys.exit("M E G A E X I T")

    elif command == "testcolor":
        warn("test")
        error("test")
        success('test')

    elif command == "logout":
        logins.logout()

    elif command == "license":
            with open('LICENSE.txt') as file:
                print(file.read())

    elif command == "createFile":
        try:
            command = command.split(" ", 2)
            file = command[1]
            file_extension = ".txt" if file[-5:] not in (".txt", ".py", ".c", ".rc", ".java") else "" # Basically if the final 5 characters in the user string are not in the tuple, then file_extension = "" as command[1] will already have a file_extension
            with open(f"{file}{file_extension}", "w") as file:
                file.write("") # Writing nothing to the file so we can just create an empty file
            command = " ".join(command, 2)
        except Exception as Err: # If we get an index error, we know that the user most likely hasn't specified a filename
            print(f"Please specify a filename!") if type(Err) == IndexError else print(f"CreateFileError: {Err}") # Printing first statement if Err is an index error, else we print the other statement

    elif command in ("quit", "exit"):
        animlib.loadingAnim("exit", 5)
        print("terminated main task. exit")
        sys.exit()

    elif command not in cmdList:
        print(f"{command} is not a valid command!")
        continue
