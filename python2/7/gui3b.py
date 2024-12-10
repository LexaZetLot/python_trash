import sys
from tkinter import *

widget = Button(None, text='Hello event world', command=(lambda: print('Hello lamda world') or sys.exit()))
widget.pack()
widget.mainloop()