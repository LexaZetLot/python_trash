import os, time, sys
mypid     = os.getpid()
parentpid = os.getppid()
sys.stderr.write('Child %d of %d got arg: "%s"\n' % (mypid, parentpid, 'pipes.py'))
for i in range(2):
    time.sleep(3)
    recv = input()
    time.sleep(3)
    send = 'Child %d got: [%s]' % (mypid, recv)
    print(send)
    sys.stdout.flush()