from tkinter import mainloop
from tkinter.messagebox import showinfo
from tkinter102 import MyGui

class CustomGui(MyGui):
    def __init__(self):
        showinfo(title='popup', message='Ouch!')

if __name__ == '__main__':
    CustomGui().pack()
    mainloop()