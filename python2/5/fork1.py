import os

def child():
    print('hello from child', os.getpid())

def parent():
    while True:
        new_pid = os.fork()
        if new_pid:
            child()
        else:
            print('hello from parent', os.getpid(), new_pid)
        if input() == 'q': break

parent()