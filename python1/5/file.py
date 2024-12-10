import sys

s = 'a\nb\tc'
print(s)
print(len(s))

mantra = """
Always look
on the bright
side of life."""
print(mantra)

myjob = "hacker"
for c in myjob: print(c, end=' ')
print("k" in myjob)
print("z" in myjob)
print("spam" in 'abcspamdef')

S = 'spam'
print(S[0], S[-2])
print(S[1:3], S[1:], S[:-1])

S = 'abcdefghijklmnop'
print(S[1:10:2])
print(S[::2])

print('spam'[1:3])
print('spam'[slice(1, 3)])
print('spam'[::-1])
print('spam'[slice(None, None, -1)])

print(str('spam'), repr('spam'))

B = '1101'
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print(I)

print(int('1101', 2))
print('That is %d %s bird!' % (1, 'dead'))
print('That is {0} {1} bird!'.format(1, 'dead'))

print('aa$bb$cc$dd'.replace('$', 'SPAM'))
S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.find('SPAM'))
print('aa$bb$cc$dd'.replace('$', 'SPAM', 1))

S = 'spammy'
L = list(S)
L[3] = 'x'
L[4] = 'x'
S = ''.join(L)
print(S)
print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))

line = 'aaa bbb ccc'
cols = line.split()
print(cols)

line = "The knights who say Ni!\n"
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))

exclamation = 'Ni'
print('The knights who say %s?' % exclamation)
print('%d %s %g you' % (1, 'spam', 4.0))
print('%s — %s — %s' % (42, 3.14159, [1, 2, 3]))

print('%(qty)d more %(food)s' % {'qty': 1, 'food': 'spam'})
reply = """
Greetings...
Hello %(name)s!
Your age is %(age)s
"""
values = {'name': 'Bob', 'age': 40}
print(reply % values)
food = 'spam'
qty = 10
vars()
print('%(qty)d more %(food)s' % vars())

print('Му {map[kind]} runs {sys.platform}'.format(sys=sys, map={'kind': 'laptop'}))
somelist = list('SPAM')
print('first = {0[0]}, third={0[2]}'.format(somelist))
print('first = {0}, third={1}'.format(somelist[0], somelist[-1]))
path = somelist[0], somelist[-1], somelist[1:3]
print('first={0}, last={1}, middle={2}'.format(*path))