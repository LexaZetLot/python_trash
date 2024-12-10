import os, sys, time

def counter(count):
    for x in range(count):
        time.sleep(1)
        print('[%s] => %s' % (os.getpid(), x))

for i in range(5):
    pid = os.fork()
    if pid != 0:
       print('Process %d spawned ' % pid)
    else:
        counter(5)
        os._exit(0)

print('Main process exiting.')