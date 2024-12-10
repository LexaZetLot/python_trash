import os
from subprocess import Popen, PIPE, call

print(os.system('python testexit_sys.py') >> 8)
print(os.system('python testexit_os.py') >> 8)

pipe = os.popen('python testexit_sys.py')
print(pipe.read())
print(pipe.close() >> 8)
pipe = os.popen('python testexit_os.py')
print(pipe.read())
print(pipe.close() >> 8)

