import sys, time, os, glob, launchmodes
from tkinter import *

InternetMode = '-live'


from windows import MainWindow
from windows import PopupWindow
Root = MainWindow('PP4E Demos 2.1')


Stat = PopupWindow('PP4E demo info')
Stat.protocol('WM_DELETE_WINDOW', lambda:0)      # ignore wm delete

Info = Label(Stat, text = 'Select demo',
             font=('courier', 20, 'italic'), padx=12, pady=12, bg='lightblue')
Info.pack(expand=YES, fill=BOTH)


from textEditor import TextEditorMainPopup

# demo launcher class
class Launcher(launchmodes.PortableLauncher):
    def announce(self, text):
        Info.config(text=text)

def viewer(sources):
    for filename in sources:
        TextEditorMainPopup(Root, filename,
                            loadEncode='utf-8')

def demoButton(name, what, doit, code, launcher=Launcher):
    rowfrm = Frame(Root)
    rowfrm.pack(side=TOP, expand=YES, fill=BOTH)

    b = Button(rowfrm, bg='navy', fg='white', relief=RIDGE, border=4)
    b.config(text=name, width=20, command=launcher(what, doit))
    b.pack(side=LEFT, expand=YES, fill=BOTH)

    b = Button(rowfrm, bg='beige', fg='navy')
    b.config(text='code', command=(lambda: viewer(code)))
    b.pack(side=LEFT, fill=BOTH)

demoButton(name='PyEdit',
           what='Text file editor',
           doit='Gui/TextEditor/textEditor.py PyDemos.pyw',
           code=['launchmodes.py',
                 'Tools/find.py',
                 'Gui/Tour/scrolledlist.py',
                 'Gui/ShellGui/formrows.py',
                 'Gui/Tools/guimaker.py',
                 'Gui/TextEditor/textConfig.py',
                 'Gui/TextEditor/textEditor.py'])

demoButton(name='PyView',
           what='Image slideshow, plus note editor',
           doit='Gui/SlideShow/slideShowPlus.py Gui/gifs',
           code=['Gui/Texteditor/textEditor.py',
                 'Gui/SlideShow/slideShow.py',
                 'Gui/SlideShow/slideShowPlus.py'])

demoButton(name='PyDraw',
           what='Draw and move graphics objects',
           doit='Gui/MovingPics/movingpics.py Gui/gifs',
           code=['Gui/MovingPics/movingpics_threads.py',
                 'Gui/MovingPics/movingpics_after.py',
                 'Gui/MovingPics/movingpics.py'])

demoButton(name='PyTree',
           what='Tree data structure viewer',
           doit='Dstruct/TreeView/treeview.py',
           code=['Lang/Parser/parser2.py',
                 'Dstruct/Classics/btree.py',
                 'Dstruct/TreeView/treeview_wrappers.py',
                 'Dstruct/TreeView/treeview.py'])

demoButton(name='PyClock',
           what='Analog/digital clocks',
           doit='Gui/Clock/clockStyles.py Gui/gifs',
           code=['Gui/Tools/windows.py',
                 'Gui/Clock/clockStyles.py',
                 'Gui/Clock/clock.py'])

demoButton(name='PyToe',
           what='Tic-tac-toe game (AI)',
           doit='Ai/TicTacToe/tictactoe.py',
           code=['Ai/TicTacToe/tictactoe_lists.py',
                 'Ai/TicTacToe/tictactoe.py'])

demoButton(name='PyForm',
           what='Persistent table viewer/editor',
           doit='Dbase/TableBrowser/formgui.py',
          #doit='Dbase/TableBrowser/formtable.py
          #doit='Dbase/TableBrowser/formtable.py
           code=['Dbase/TableBrowser/formtable.py',
                 'Dbase/TableBrowser/formgui.py'])

demoButton(name='PyCalc',
           what='Calculator, plus extensions',
           doit='Lang/Calculator/calculator_plusplus.py',
           code=['Lang/Calculator/calculator_plusplus.py',
                 'Lang/Calculator/calculator_plus_ext.py',
                 'Lang/Calculator/calculator_plus_emb.py',
                 'Lang/Calculator/calculator.py'])

demoButton(name='PyFtp',
           what='Python+Tk ftp clients',
           doit='Internet/Ftp/PyFtpGui.pyw',
           code=['Internet/Sockets/form.py',
                 'Internet/Ftp/putfile.py',
                 'Internet/Ftp/getfile.py',
                 'Internet/Ftp/putfilegui.py',
                 'Internet/Ftp/getfilegui.py',
                 'Internet/Ftp/PyFtpGui.pyw'])


demoButton(name='PyPhoto',
           what='PIL thumbnail image viewer',
           doit='Gui/PIL/pyphoto1.py Gui/PIL/images',
           code=['Gui/PIL/viewer_thumbs.py',
                 'Gui/PIL/pyphoto1.py',
                 'PyDemos-pil-note.txt'])


locat  = 'Internet/Email'
locat2 = locat + '/PyMailGui'

saved  = '%s/SavedMail/savemany-3E.txt' % locat2
saved += ' %s/SavedMail/i18n-4E %s/SavedMail/version30-4E' % (locat2, locat2)

source = glob.glob(locat + '/mailtools/*.py')
source+= glob.glob(locat + '/PyMailGui/*.py')
source+= glob.glob(locat + '/PyMailGui/*.html')
source = [F for F in source if not (
                      os.path.basename(F)[0] == '_' and
                      os.path.basename(F)[:2] != '__')]  # del tests

demoButton(name='PyMailGUI',
           what='Python+Tk pop/smtp email client',
           doit='%s/PyMailGui.py %s' % (locat2, saved),
           code=(['Gui/Texteditor/textEditor.py',
                  'Gui/Tools/windows.py',
                  'Gui/Tools/threadtools.py'] + source) )

pagepath = os.getcwd() + '/Internet/Web'
pymailcgifiles = (glob.glob('Internet/Web/PyMailCgi/cgi-bin/*.py') +
                  ['Internet/Web/PyMailCgi/pymailcgi.html'])

if InternetMode == '-file':
    demoButton('PyMailCGI',
               'Browser-based pop/smtp email interface',
               'LaunchBrowser.pyw -file %s/PyMailCgi/pymailcgi.html' % pagepath,
               pymailcgifiles)

    demoButton('PyInternet',
               'Internet-based demo launcher page',
               'LaunchBrowser.pyw -file %s/PyInternetDemos.html' % pagepath,
               ['%s/PyInternetDemos.html' % pagepath])

else:
    web80_started = web8000_started = False

    def startLocalWebServers(port):
        global web80_started, web8000_started
        onWin   = sys.platform.startswith('win')
        spawner = launchmodes.StartArgs if onWin else launchmodes.PortableLauncher

        if port == 80 and not web80_started:
            web80_started = True
            spawner('server80',
                    'Internet/Web/webserver.py Internet/Web')()

        elif port == 8000 and not web8000_started:
            web8000_started = True
            spawner('server8000',
                    'Internet/Web/webserver.py Internet/Web/PyMailCgi 8000')()

    site = 'localhost:%s'

    class WebLauncher(Launcher):
        def run(self, cmdline):
            port, cmdline = cmdline.split('@')
            startLocalWebServers(int(port))
            Launcher.run(self, cmdline)

    demoButton('PyMailCGI',
               'Browser-based pop/smtp email interface',
               '8000@LaunchBrowser.pyw -live pymailcgi.html '+ (site % 8000),
               ['%s/webserver.py' % pagepath] + pymailcgifiles,
               launcher=WebLauncher)

    demoButton('PyInternet',
               'Main Internet demos launcher page',
               '80@LaunchBrowser.pyw -live PyInternetDemos.html ' + (site % 80),
               ['%s/webserver.py' % pagepath,
                '%s/PyInternetDemos.html' % pagepath],
                launcher=WebLauncher)


def refreshMe(info, ncall):
    slant = ['normal', 'italic', 'bold', 'bold italic'][ncall % 4]
    info.config(font=('courier', 20, slant))
    Root.after(1000, (lambda: refreshMe(info, ncall+1)) )


Stat.iconify()
def onInfo():
    if Stat.state() == 'iconic':
        Stat.deiconify()
    else:
        Stat.iconify()


radiovar = StringVar()

def onLinks():
    popup = PopupWindow('PP4E web site links')
    links = [("Book",
                   'LaunchBrowser.pyw -live about-pp.html www.rmi.net/~lutz'),
             ("Python",
                   'LaunchBrowser.pyw -live index.html www.python.org'),
             ("O'Reilly",
                   'LaunchBrowser.pyw -live index.html www.oreilly.com'),
             ("Author",
                   'LaunchBrowser.pyw -live index.html www.rmi.net/~lutz')]

    for (name, command) in links:
        callback = Launcher((name + "'s web site"), command)
        link = Radiobutton(popup, text=name, command=callback)
        link.config(relief=GROOVE, variable=radiovar, value=name)
        link.pack(side=LEFT, expand=YES, fill=BOTH)
    radiovar.set(name)
    Button(popup, text='Quit', command=popup.destroy).pack(expand=YES,fill=BOTH)

    if InternetMode != '-live':
        from tkinter.messagebox import showwarning
        showwarning('PP4E Demos', 'Web links require an Internet connection')


Button(Root, text='Info',  command=onInfo).pack(side=TOP, fill=X)
Button(Root, text='Links', command=onLinks).pack(side=TOP, fill=X)
Button(Root, text='Quit',  command=Root.quit).pack(side=BOTTOM, fill=X)
refreshMe(Info, 0)
Root.mainloop()