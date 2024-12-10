import sys
from tkinter import *
makemodal = False

def dialog():
    win = Toplevel()
    Label(win,  text='Hard drive reformatted!').pack()
    Button(win, text='OK', command=win.destroy).pack()
    if makemodal:
        win.focus_set()
        win.grab_set()
        win.wait_window()
    print('dialog exit')

root = Tk()
Button(root, text='popup', command=dialog).pack()
root.mainloop()