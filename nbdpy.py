import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from boxEngine import *
from sys import *
from rich.console import Console

console = Console()
boxVarMessage = "nbdpy message"
console.print(f"["+"[bold][bright_green] OK [/]"+"]"+"[italic] BPS GUI is loaded!")

class nbDisplay:
    def startDisplay():
        #root code
        print("close window to continue shell task")
        root = tk.Tk()
        print("tk initiated")
        root.geometry("600x300")

        title= Label(root,text="shell display",font="sans 24 bold")
        title.grid(row=0,column=2)

        made_by= Label(root,text="by ValkTheBoxman!",font="sans 15 bold")
        made_by.grid(row=0,column=4)

        def hello1():
            messagebox.showinfo(boxVarMessage, "Hello, World!")

        def hello2():
            print("Hello, World!")

        def joke():
            messagebox.askyesno(boxVarMessage,"ok?")
            messagebox.showinfo(boxVarMessage,"oh ok, wont judge your choice")

        def clearscreen():
            messagebox.showinfo(boxVarMessage,"Ok, i will clear the screen")
            spamClear()

        def megaExit():
            sys.exit("MegaExited through the nbdpy display. Thanks for using it!")

        def HWrep():
            count = 0
            messagebox.showwarning(boxVarMessage," Use KeyboardInterrupt (Ctrl+C) to stop it! ")

            rune = True
            while rune:
                print("Hello, world! ", count)
                count += 1


        helloworld = Button(root, text = "Say Hello, World!", command = hello1)
        helloworld.place(x = 35, y = 50)

        jokeBt = Button(root, text="click for a joke", command=joke)
        jokeBt.place(x = 35, y = 90)

        spamClearBt = Button(root, text="Clear Shell", command=clearscreen)
        spamClearBt.place(x = 97, y = 50)

        helloworld2 = Button(root, text = "Print Hello, World!", command = hello2)
        helloworld2.place(x = 205, y = 90)

        megaExitBt = Button(root, text = "MegaExit", command = megaExit)
        megaExitBt.place(x = 35, y = 150)

        hwrepchk = Checkbutton(root, text= "spam hello world", command = HWrep)
        hwrepchk.place(x = 100, y = 100)

        root.mainloop()
