from tkinter import *
from calc0 import CalcGui

class Inner(CalcGui):
    def __init__(self):
        CalcGui.__init__(self)
        Label(self,  text='Calc Subclass').pack()
        Button(self, text='Quit', command=self.quit).pack()

Inner().mainloop()