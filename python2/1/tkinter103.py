from tkinter import *
from tkinter.messagebox import showinfo

def reply(name):
    showinfo(title='Reply', message='Hello %s!' % name)

top = Tk()
top.title('Echo')
top.iconbitmap('py-blue-trans-out.ico')

Label(top, text='Event your name:').pack(side=TOP)
ent = Entry(top)
ent.pack(side=TOP)
btn = Button(top, text='Submit', command=lambda: reply(ent.get()))
btn.pack(sode=LEFT)

top.mainloop()