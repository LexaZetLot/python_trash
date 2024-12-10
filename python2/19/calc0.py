from tkinter import *
from widgets import frame, button, entry

class CalcGui(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Python Calculator 0.1')
        self.master.iconname("pcalc1")

        self.names = {}
        text = StringVar()
        entry(self, TOP, text)

        rows = ["abcd", "0123", "4567", "89()"]
        for row in rows:
            frm = frame(self, TOP)
            for char in row:
                button(frm, LEFT, char,
                            lambda char=char: text.set(text.get() + char))

        frm = frame(self, TOP)
        for char in "+-*/=":
            button(frm, LEFT, char,
                        lambda char=char: text.set(text.get()+ ' ' + char + ' '))

        frm = frame(self, BOTTOM)
        button(frm, LEFT, 'eval',  lambda: self.eval(text) )
        button(frm, LEFT, 'clear', lambda: text.set('') )

    def eval(self, text):
        try:
            text.set(str(eval(text.get(), self.names, self.names)))    # was 'x'
        except SyntaxError:
            try:
                exec(text.get(), self.names, self.names)
            except:
                text.set("ERROR")
            else:
                text.set('')
        except:
            text.set("ERROR")

if __name__ == '__main__': CalcGui().mainloop()