from tkinter import *
from calc0 import CalcGui

class Outer:
    def __init__(self, parent):
        Label(parent, text='Calc Attachment').pack()
        CalcGui(parent)
        Button(parent, text='Quit', command=parent.quit).pack()

root = Tk()
Outer(root)
root.mainloop()