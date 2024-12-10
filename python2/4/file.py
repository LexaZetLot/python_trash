import sys

lines = [line.rstrip() for line in open('data.txt')]
print(lines)

lines = list(map(str.split, open('data.txt')))
print(lines)

file = open('data.txt', 'a')
file.write('asdasdas')
file.close()

print(open('data.txt').read())

open('data.bin', 'wb').write(b'asdasdas')
print(open('data.bin', 'rb').read())

import struct
data = struct.pack('>i4shf', 2, b'spam', 3, 1.234)
print(data)
file = open('data.bin', 'wb')
file.write(data)
file.close()

print(open('data.bin', 'rb').read())
value = struct.unpack('>i4shf', open('data.bin', 'rb').read())
print(value)


for stream in (sys.stdin, sys.stdout, sys.stderr):
    print(stream.fileno())

print(sys.stdout.write('hello stdio world\n'))

import os
os.write(1, b'Hello descriptor world\n')

fp = open('data.txt', 'w')
fd = fp.fileno()
os.write(fd, b'Hello descriptor world\n')


fdfile = os.open(r'data.txt', os.O_RDWR | os.O_CLOEXEC)
print(fdfile)

info = os.stat('data.txt')
print(info)
print(info.st_mode, info.st_size)

for (dirname, subshere, fileshere) in os.walk('.'):
    print('[' + dirname + ']')
    for fname in fileshere:
        print(os.path.join(dirname, fname))