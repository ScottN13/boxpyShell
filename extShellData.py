from tkinter import *

# cmd items not worth putting there
cmdList = ["shellBasic","source","pyclockInit","passgenInit","help","quit","exit"]

class pythonBasic:
    class functions:
        def length():
            string = input()
            len(string)
        def identify():
            string = input()
            id(string)
    class screens:
        print("close to continue your pyhub task")
        def createScreen():
            #self explanatory
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