import os
from tkinter import *
import random
import time
import sys

# cmd items not worth putting there
cmdList = ["shellBasic","source","pyclockInit","passgenInit","help","quit","exit","nbdpy"]
scrCMDlist = ["t","ti","help","tc","pc","back"]

print("extShell data init")

#data
ver = "1.5.11.22" # The first two digits stand for build number, the 2nd two stand for month and year.
 
def spamClear():
    for i in range(100):
        print("")

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
    class screens:
        def createScreen():
            run = TRUE
            while run:
                print("close to continue your shell task")
                #self explanatory
                print("Choose what should pop up? (text,image,etc.)")
                inputWish = input()
                if inputWish == "t":
                    print("Input a text message to show up on the screen")
                    labelName = input()
                    print("exit window to continue your tasks")

                    #tkinter window data
                    root=Tk()
                    root.geometry("600x300")
                    #label
                    cusLabel=Label(root,text=labelName,font="times 24 bold")
                    cusLabel.grid(row=0,column=2)
                    
                    #nota=Label(root,text="",font="times 15 bold")
                    #nota.grid(row=3,column=2)
                    root.mainloop()
                break
                
                if inputWish != scrCMDlist:
                    print("COMMAND IS WRONG")
                    continue

class extFunc:
    class funct:
        def echo(x):
            print(x)
        
        def shellVer():          
            print(f"boxpyshell created by ValkTheBoxman\nver: {ver} Build: main\n（＾ω＾）\n")
            

    class math:
        def add():
            num1 = input("What is your first number? -> ")
            num2 = input("What is your second number? -> ")
            print(f"adding {num1} + {num2})
            print(int(num1) + int(num2))
        
        def subtract():
            num1 = input("What is your first number? -> ")
            num2 = input("What is your second number? -> ")
            print(f"subtracting {num1} - {num2})
            print(int(num1) - int(num2))

    class fun:
        def helloUser():
            print("What is your name?")
            name = input()
            print("Hello!,",name)
        
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
