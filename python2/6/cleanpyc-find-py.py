import os, sys, find

count = 0
for filename in find.find('*.pyc', sys.argv[1]):
    count += 1
    print(filename)
    

print('Removed %d .pyc files' % count)