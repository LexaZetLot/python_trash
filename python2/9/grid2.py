from tkinter import *
colors = ['red', 'green', 'orange', 'white', 'yellow', 'blue']

def gridbox(parent):
    row = 0
    for color in colors:
        lab = Label(parent, text=color, relief=RIDGE,  width=25)
        ent = Entry(parent, bg=color,   relief=SUNKEN, width=50)
        lab.grid(row=row, column=0)
        ent.grid(row=row, column=1)
        ent.insert(0, 'grid')
        row += 1

def packbox(parent):
    for color in colors:
        row = Frame(parent)
        lab = Label(row, text=color, relief=RIDGE,  width=25)
        ent = Entry(row, bg=color,   relief=SUNKEN, width=50)
        row.pack(side=TOP)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT)
        ent.insert(0, 'pack')

if __name__ == '__main__':
    root = Tk()
    gridbox(Toplevel())
    packbox(Toplevel())
    Button(root, text='Quit', command=root.quit).pack()
    mainloop()