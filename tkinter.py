

from tkinter import *

root = Tk()

def OpenPro1():

    print("Hej")

    execfile('runthis.py') #write any file with .py extension.This method is similar to rightclick and open

button_1 = Button(root, text = "Hejdå", command = OpenPro1)

button_1.pack()


root.mainloop()

