import sys

def getreply():
    if sys.stdin.isatty():
        return input('?')
    else:
        platform = sys.platform[:3]

        if platform == 'win':
            import mscvrt
            mscvrt.putch(b'?')
            key = mscvrt.getche()
            mscvrt.putch(b'\n')
            return key
        elif platform == 'cyg':
            open('/dev/tty', 'w').write('?')
            key = open('/dev/tty').readline()[:-1]
            return key
        else:
            assert False, "platform '%s' not supported" % platform

def more(text, numlines=10):
    lines = text.splitlines()
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk: print(line)
        if lines and getreply() not in [b'y', b'Y', 'y', 'Y']: break

if __name__ == '__main__':
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())