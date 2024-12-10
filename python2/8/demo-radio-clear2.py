from tkinter import *
root = Tk()

def radio1(root):
    tmp = IntVar()
    for i in range(10):
        rad = Radiobutton(root, text=str(i), value=i, variable=tmp)
        rad.pack(side=LEFT)
    tmp.set(5)

def radio2(root):
    global var
    var  = IntVar()
    for i in range(10):
        rad = Radiobutton(root, text=str(i), value=i, variable=var)
        rad.pack(side=LEFT)
    var.set(2)

def ondel():
    global var
    del var

frm = Frame(); frm.pack(); radio1(frm)
frm = Frame(); frm.pack(); radio2(frm)
Button(root, text='del', command=ondel).pack()
root.mainloop()