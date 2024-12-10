import sys

nudge = 1
wink = 2
a, b = nudge, wink
print(a, b)
[c, d] = [nudge, wink]
print(c, d)

string = 'spam'
a, b, c, d = string
print(a, b, c, d)

L = [1, 2, 3, 4]
while L:
    front, L = L[0], L[1:]
    print(front, L)


seq = [1,2,3,4]
a, b, c, d = seq
print(a, b, c, d)
a, *b = seq
print(a, b)
*a, b = seq
print(a, b)
a, *b, c = seq
print(a, b, c)

L = [1, 2, 3, 4]
while L:
    front, *L = L
    print(front, L)

a = b = []
b.append(42)
print(a, b)

a = []
b = []

temp = sys.stdout
sys.stdout = open('log.txt', 'a')
print('spam')
print(1, 2, 3)
sys.stdout.close()
sys.stdout = temp
print(a, b)
print(open('log.txt').read())

log =open('log.txt', 'w')
print('spam', file=log)
print('spam123123', file=log)
log.close()
print(843219)
print(open('log.txt').read())
