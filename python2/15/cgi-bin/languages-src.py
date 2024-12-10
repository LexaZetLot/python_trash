import cgi
filename = 'cgi-bin/languages.py'

print('Content-type: text/html\n')
print('<TITLE>Languages</TITLE>')
print("<H1>Source code: '%s'</H1>" % filename)
print('<HR><PRE>')
print(cgi.escape(open(filename).read()))    
print('</PRE><HR>')