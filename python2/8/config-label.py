from tkinter import *

root = Tk()
labelfront = ('times', 20, 'bold')
widget = Label(root, text='Hello Config world')
widget.config(bg='black', fg='yellow')
widget.config(font=labelfront)
widget.config(height=3, width=20)
widget.pack(expand=YES, fill=BOTH)
root.mainloop()