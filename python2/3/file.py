import sys, os
print('my os.getcwd =>', os.getcwd())
print('my sys.path =>', sys.path[:6])

for f in (sys.stdin, sys.stdout, sys.stderr):
    print(f)

