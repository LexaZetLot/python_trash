import subprocess
import sys, os
print(len(dir(sys)))
print(len(dir(os)))

print(len(dir(os.path)))

print(dir(sys))
print(dir(os))

help(sys)
print(sys.__doc__)

mystr = 'xxxSPAMxxx'
print(mystr.find('SPAM'))
mystr = 'xxxaaxxxaa'
print(mystr.replace('aa', 'SPAM'))
print('SPAM' in mystr)
mystr = '\tNi\n'
print(mystr.strip())
print(mystr.rstrip())


mystr = 'ASDASDSADASD'
print(mystr.lower())
print(mystr.isalpha())
print(mystr.isdigit())

import string
print(string.ascii_lowercase)
repr(string.whitespace)

mystr = 'aaa,bbb,ccc'
print(mystr.split(','))

delim = 'Ni'
print(delim.join(['aaa', 'bbb', 'ccc']))

import sys
print(sys.platform, sys.maxsize, sys.version)
print(sys.path)
print(sys.modules)
print(list(sys.modules.keys()))
print(sys.modules['sys'])

import traceback, sys
def grail(x):
    raise TypeError('already got one')

# try:
#     grail('arthur')
# except:
#     exc_infp = sys.exc_info()
#     print(exc_infp[0])
#     print(exc_infp[1])
#     traceback.print_tb(exc_infp[2])

print(os.getpid())
print(os.getcwd())
print(os.pathsep, os.sep, os.pardir, os.curdir, os.linesep)

lesting = os.popen('dir /').readlines()
print(lesting)

pipe = subprocess.Popen('dir /', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(pipe.communicate())
