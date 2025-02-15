debugme  = False                                 
inputkey = 'language'

hellos = {
    'Python':    r" print('Hello World')               ",
    'Python2':   r" print 'Hello World'                ",
    'Perl':      r' print "Hello World\n";             ',
    'Tcl':       r' puts "Hello World"                 ',
    'Scheme':    r' (display "Hello World") (newline)  ',
    'SmallTalk': r" 'Hello World' print.               ",
    'Java':      r' System.out.println("Hello World"); ',
    'C':         r' printf("Hello World\n");           ',
    'C++':       r' cout << "Hello World" << endl;     ',
    'Basic':     r' 10 PRINT "Hello World"             ',
    'Fortran':   r" print *, 'Hello World'             ",
    'Pascal':    r" WriteLn('Hello World');            "
}

class dummy:
    def __init__(self, str): self.value = str

import cgi, sys
if debugme:
    form = {inputkey: dummy(sys.argv[1])}
else:
    form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<TITLE>Languages</TITLE>')
print('<H1>Syntax</H1><HR>')

def showHello(form):
    choice = form[inputkey].value
    print('<H3>%s</H3><P><PRE>' % choice)
    try:
        print(cgi.escape(hellos[choice]))
    except KeyError:
        print("Sorry--I don't know that language")
    print('</PRE></P><BR>')

if not inputkey in form or form[inputkey].value == 'All':
    for lang in hellos.keys():
        mock = {inputkey: dummy(lang)}
        showHello(mock)
else:
    showHello(form)
print('<HR>')