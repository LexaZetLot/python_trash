import _thread as thread, time

def counter(myId, count):
    for i in range(count):
        time.sleep(1)
        print('[%s] => %s' % (myId, i))

for i in range(10):
    thread.start_new_thread(counter, (i, 5))

time.sleep(5)
print('Main thread done')