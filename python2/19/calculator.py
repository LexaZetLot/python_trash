from tkinter import *
from guimixin import GuiMixin
from widgets import label, entry, button, frame
Fg, Bg, Font = 'black', 'skyblue', ('courier', 14, 'bold')

debugme = True
def trace(*args):
    if debugme: print(args)



class CalcGui(GuiMixin, Frame):
    Operators = "+-*/="
    Operands  = ["abcd", "0123", "4567", "89()"]

    def __init__(self, parent=None, fg=Fg, bg=Bg, font=Font):
        Frame.__init__(self, parent)
        self.pack(expand=YES, fill=BOTH)
        self.eval = Evaluator()
        self.text = StringVar()
        self.text.set("0")
        self.erase = 1
        self.makeWidgets(fg, bg, font)
        if not parent or not isinstance(parent, Frame):
            self.master.title('PyCalc 3.0')
            self.master.iconname("PyCalc")
            self.master.bind('<KeyPress>', self.onKeyboard)
            self.entry.config(state='readonly')
        else:
            self.entry.config(state='normal')
            self.entry.focus()

    def makeWidgets(self, fg, bg, font):
        self.entry = entry(self, TOP, self.text)
        self.entry.config(font=font)
        self.entry.config(justify=RIGHT)
        for row in self.Operands:
            frm = frame(self, TOP)
            for char in row:
                button(frm, LEFT, char,
                            lambda op=char: self.onOperand(op),
                            fg=fg, bg=bg, font=font)

        frm = frame(self, TOP)
        for char in self.Operators:
            button(frm, LEFT, char,
                        lambda op=char: self.onOperator(op),
                        fg=bg, bg=fg, font=font)

        frm = frame(self, TOP)
        button(frm, LEFT, 'dot ', lambda: self.onOperand('.'))
        button(frm, LEFT, ' E+ ', lambda: self.text.set(self.text.get()+'E+'))
        button(frm, LEFT, ' E- ', lambda: self.text.set(self.text.get()+'E-'))
        button(frm, LEFT, 'cmd ', self.onMakeCmdline)
        button(frm, LEFT, 'help', self.help)
        button(frm, LEFT, 'quit', self.quit)

        frm = frame(self, BOTTOM)
        button(frm, LEFT, 'eval ', self.onEval)
        button(frm, LEFT, 'hist ', self.onHist)
        button(frm, LEFT, 'clear', self.onClear)

    def onClear(self):
        self.eval.clear()
        self.text.set('0')
        self.erase = 1

    def onEval(self):
        self.eval.shiftOpnd(self.text.get())
        self.eval.closeall()
        self.text.set(self.eval.popOpnd())
        self.erase = 1

    def onOperand(self, char):
        if char == '(':
            self.eval.open()
            self.text.set('(')
            self.erase = 1
        elif char == ')':
            self.eval.shiftOpnd(self.text.get())
            self.eval.close()
            self.text.set(self.eval.popOpnd())
            self.erase = 1
        else:
            if self.erase:
                self.text.set(char)
            else:
                self.text.set(self.text.get() + char)
            self.erase = 0

    def onOperator(self, char):
        self.eval.shiftOpnd(self.text.get())
        self.eval.shiftOptr(char)
        self.text.set(self.eval.topOpnd())
        self.erase = 1

    def onMakeCmdline(self):
        new = Toplevel()
        new.title('PyCalc command line')
        frm = frame(new, TOP)
        label(frm, LEFT, '>>>').pack(expand=NO)
        var = StringVar()
        ent = entry(frm, LEFT, var, width=40)
        onButton = (lambda: self.onCmdline(var, ent))
        onReturn = (lambda event: self.onCmdline(var, ent))
        button(frm, RIGHT, 'Run', onButton).pack(expand=NO)
        ent.bind('<Return>', onReturn)
        var.set(self.text.get())

    def onCmdline(self, var, ent):
        try:
            value = self.eval.runstring(var.get())
            var.set('OKAY')
            if value != None:
                self.text.set(value)
                self.erase = 1
                var.set('OKAY => '+ value)
        except:
            var.set('ERROR')
        ent.icursor(END)
        ent.select_range(0, END)

    def onKeyboard(self, event):
        pressed = event.char
        if pressed != '':
            if pressed in self.Operators:
                self.onOperator(pressed)
            else:
                for row in self.Operands:
                    if pressed in row:
                        self.onOperand(pressed)
                        break
                else:
                    if pressed == '.':
                        self.onOperand(pressed)
                    if pressed in 'Ee':  # 2e10, no +/-
                        self.text.set(self.text.get()+pressed)
                    elif pressed == '\r':
                        self.onEval()
                    elif pressed == ' ':
                        self.onClear()
                    elif pressed == '\b':
                        self.text.set(self.text.get()[:-1])
                    elif pressed == '?':
                        self.help()

    def onHist(self):
        from tkinter.scrolledtext import ScrolledText
        new = Toplevel()
        ok = Button(new, text="OK", command=new.destroy)
        ok.pack(pady=1, side=BOTTOM)
        text = ScrolledText(new, bg='beige')
        text.insert('0.0', self.eval.getHist())
        text.see(END)
        text.pack(expand=YES, fill=BOTH)

        new.title("PyCalc History")
        new.bind("<Return>", (lambda event: new.destroy()))
        ok.focus_set()
        new.grab_set()
        new.wait_window()

    def help(self):
        self.infobox('PyCalc', 'PyCalc 3.0+\n'
                               'A Python/tkinter calculator\n'
                               'Programming Python 4E\n'
                               'May, 2010\n'
                               '(3.0 2005, 2.0 1999, 1.0 1996)\n\n'
                               'Use mouse or keyboard to\n'
                               'input numbers and operators,\n'
                               'or type code in cmd popup')

class Evaluator:
    def __init__(self):
        self.names = {}
        self.opnd, self.optr = [], []
        self.hist = []
        self.runstring("from math import *")
        self.runstring("from random import *")

    def clear(self):
        self.opnd, self.optr = [], []
        if len(self.hist) > 64:
            self.hist = ['clear']
        else:
            self.hist.append('--clear--')

    def popOpnd(self):
        value = self.opnd[-1]
        self.opnd[-1:] = []
        return value

    def topOpnd(self):
        return self.opnd[-1]

    def open(self):
        self.optr.append('(')

    def close(self):
        self.shiftOptr(')')
        self.optr[-2:] = []

    def closeall(self):
        while self.optr:
            self.reduce()
        try:
            self.opnd[0] = self.runstring(self.opnd[0])
        except:
            self.opnd[0] = '*ERROR*'

    afterMe = {'*': ['+', '-', '(', '='],
               '/': ['+', '-', '(', '='],
               '+': ['(', '='],
               '-': ['(', '='],
               ')': ['(', '='],
               '=': ['('] }

    def shiftOpnd(self, newopnd):
        self.opnd.append(newopnd)

    def shiftOptr(self, newoptr):
        while (self.optr and
               self.optr[-1] not in self.afterMe[newoptr]):
            self.reduce()
        self.optr.append(newoptr)

    def reduce(self):
        trace(self.optr, self.opnd)
        try:
            operator       = self.optr[-1]
            [left, right]  = self.opnd[-2:]
            self.optr[-1:] = []
            self.opnd[-2:] = []
            result = self.runstring(left + operator + right)
            if result == None:
                result = left
            self.opnd.append(result)
        except:
            self.opnd.append('*ERROR*')

    def runstring(self, code):
        try:
            result = str(eval(code, self.names, self.names))
            self.hist.append(code + ' => ' + result)
        except:
            exec(code, self.names, self.names)
            self.hist.append(code)
            result = None
        return result

    def getHist(self):
        return '\n'.join(self.hist)

def getCalcArgs():
    from sys import argv
    config = {}
    for arg in argv[1:]:
        if arg in ['-bg', '-fg']:
            try:
                config[arg[1:]] = argv[argv.index(arg) + 1]
            except:
                pass
    return config

if __name__ == '__main__':
    CalcGui(**getCalcArgs()).mainloop()