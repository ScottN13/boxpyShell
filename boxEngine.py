import os
import random
import time
import platform
import sys
from configparser import ConfigParser
from rich.console import Console

console = Console()
config = ConfigParser(comment_prefixes="#", delimiters="=")
config.read("data/config/main.ini")

# Color codes:
def warn(stri: str):
    console.print(f"[bold][bright_yellow]█ Warning! -> {stri}[/]")
def error(stri: str):
    console.print(f"[bold][bright_red]█ Error! -> {stri}[/]")
def success(stri: str):
    console.print(f"[bold][bright_green]█ Success! -> {stri}[/]")

try:
    configCheck1 = str(config["DEBUG"]["disableRem"])
    if configCheck1 == "false":
        print("# Reminder!! Every command is CaSe SeNsItIvE")
    else: ...

except:
    exit("Error! Config file or an element is missing!")

# cmd items not worth putting there
cmdList = ["shellBasic","source","pyclockInit","passgenInit","help","quit","exit","vars","cvar","box"]
ver = str(config["MAIN"]["version"])
console.print(f"[ [bold][bright_green]OK[/] ][italic] boxEngine is loaded![/]")

class boxEngine:

    def box(string):
        from git import Repo
        repo = Repo()     

    def rok():
        return "Exit status:", 0
    
    def rno():
        return "Something wrong happened, exit status:",0

    def rmdir(path: str):
        os.rmdir(path)

    def mkdir(name: str):
        os.mkdir(name)

    def clear():
        if os.name() == 'nt':
            os.system("cls")
        else:
            os.system("clear")

    def cvar(): # this one wont write.
        with open('data/txt/cvar.txt', mode="w+") as file:
            print(f"cvar value = {file.read()}")
            lines = file.readlines()


        cvarI = input("cvar> ")
        if cvarI == "exit": ...
        elif cvarI == "change":
            print("Input new string or integer to change.")
            ce = input("cvar>change> ")
            with open("data/txt/cvar.txt", "wt") as file:
                for line in lines:
                    file.write(ce)
                print(f"New cvar value is:{ce}")

    def vars():
        config.read("data/config/vars.ini")
        try:
            readVars = str(config.items("VARS"))
            print("Current vars are:")
            print(readVars)
        except:
            boxEngine.error.data404()
    
    class error():
        def noCvar():
            error("File 'cvar.txt' in /data/txt/ wasn't found.")

        def NotImplement():
            warn("Sorry, but this function is not implemented yet!")

        def ConfigFatal(Err):
            console.print_exception(f"[bold][bright_red][Error!] Config file or an element is missing! -> {Err}")
        
        def data404():
            error("Data needed to access wasn't found.")

        def userFail():
            error("Input Password failed too many times.")

        def user404():
            error("User not found.")

    class funct:
        def echo(x): print(x)
        
        def shellVer(): print(f"boxpyshell created by ValkTheBoxman\nver: {ver} Build: main\n（＾ω＾）\n")


    class pc:
        def info():
            # get pc info
            uname = platform.uname()
            print(f"CPU bit:{platform.machine()}\n",f"PC OS: {platform.platform}\n",f"PC Nodename:{uname.node()}")

class animlib:
    def loadingAnim(x,y) -> None:

        top = "|"
        right = ">"
        left = "<"

        if x == "load":
            state = "loading...  "
        elif x == "exit":
            state = "exiting... "

        for i in range(y):
            print(state,top, end="\r")
            time.sleep(0.5)
            print(state,left, end="\r")
            time.sleep(0.5)
            print(state,top, end="\r")
            time.sleep(0.5)
            print(state,right, end="\r")
            time.sleep(0.5)



class pythonBasic:
    class functions:
        def length():
            print("Count the letters in a word!")
            string = input()
            len(string)
        def identify():
            string = input()
            id(string)
            

    class math:
        def add():
            num1 = input("What is your first number? -> ")
            num2 = input("What is your second number? -> ")
            print(f"adding {num1} + {num2}")
            print(int(num1) + int(num2))
        
        def subtract():
            num1 = input("What is your first number? -> ")
            num2 = input("What is your second number? -> ")
            print(f"subtracting {num1} - {num2}")
            print(int(num1) - int(num2))

    class fun:
        def helloUser():
            print("What is your name?")
            name = input()
            print(f"Hello!, {name}")
        
        def eightBall():
            print("Ask me a question and i shall give you an answer")
            ques = input(" -> ")
            list = ["Outlook Good","Outlook not so good","i cannot answer at this moment","It is certain.","It is decidedly so.","Without a doubt.","Yes definitely.","You may rely on it.","As I see it, yes.Most likely.","Yes.","Signs point to yes.","Reply hazy, try again.","Ask again later.","Better not tell you now.","Cannot predict now.","Concentrate and ask again.","Don't count on it.","My reply is no.","My sources say no.","Very doubtful."]
            ans = random.choice(list)
            print(ans)

        def ynGame():
            print("Ask me a yes or no question")
            ques = input(" -> ")
            list = ["Yes","No","Probably","Probably Not"]
            ans = random.choice(list)
            print(ans)

