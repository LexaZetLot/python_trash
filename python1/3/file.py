import math
import random
import decimal
from fractions import Fraction

print(40 + 3.14)
print(int(3.1415), float(3))

a = 3
b = 4
print(a + 1, a - 1)
print(b * 3, b / 2)
print(a % 2, b ** 2)
print(2 + 4.0, 2.0 ** b)
print(b / 2 + a)
print(b / (2.0 + a))

num = 1 / 3.0
print(num)
print('%e' % num)
print('%4.2f' % num)
print('{0:4.2f}'.format(num))

print(1 < 2)
print(2.0 >= 1)
print(2.0 == 2.0)
print(2.0 != 2.0)

X = 2
Y = 4
Z = 6
print(X < Y < Z)
print(X < Y and Y < Z)
print(X < Y > Z)
print(X < Y or Y > Z)
print(1 < 2 < 3.0 < 4)
print(1 > 2 > 3.0 > 4)

print(math.floor(2.5))
print(math.floor(-2.5))
print(math.trunc(2.5))
print(math.trunc(-2.5))

print(1j * 1J)
print(2 + 1j * 3)
print(2 + 1j * 3)

print(0o1, 0o20, 0o377)
print(0x01, 0x10, 0xFF)
print(0b1, 0b10000, 0b11111111)

print(0xFF, (15 * (16 ** 1) + (15 * (16 ** 0))))
print(0x2F, (2 * (16 ** 1) + (15 * (16 ** 0))))
print(0xF, 0b1111, (1 * (2 ** 3) + 1 * (2 ** 2) + 1 * (2 ** 1) + 1 * (2 ** 0)))

print(oct(64), hex(64), bin(64))

print(64, 0o100, 0x40, 0b10000000)
print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))
print(int('0x40', 16), int('0b1000000', 2))
print(eval('64'), eval('0o100'), eval('0x40'), eval('0b1000000'))

print('{0:o}, {1:x}, {2:b}'.format(64, 64, 64))
print('%o, %x, %x, %X' % (64, 64, 255, 255))

x = 1
print(x << 2)
print(x | 2)
print(x & 1)

x = 0b0001
print(bin(x << 2))
print(bin(x | 0b0010))
print(bin(x & 0b1))

x = 99
print(bin(x), x.bit_length(), len(bin(x)) - 2)
print(bin(256), (256).bit_length(), len(bin(256)) - 2)

print(math.sin(2 * math.pi / 180))
print(math.sqrt(144), math.sqrt(2))
print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)
print(abs(-42.0), sum((1, 2, 3, 4)))
print(min(3, 1, 2, 4), max(3, 1, 2, 4))

print(round(2.567), round(2.467), round(2.567, 2))
print('%.1f' % 2.567, '{0:.2f}'.format(2.567))
print(math.sqrt(144), 144 ** .5, pow(144, .5))

print(random.random())
print(random.randint(1, 10))
print(random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']))
suits = ['hearts', 'clubs' , 'diamonds', 'spades']
random.shuffle(suits)
print(suits)
print(0.1 + 0.1 + 0.1 - 0.3)
print(decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1') - decimal.Decimal('0.3'))
decimal.getcontext().prec = 4
print(decimal.Decimal('1') / decimal.Decimal('7'))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

x = Fraction(1, 3)
y = Fraction(4, 6)
print(x , y)
print(x + y)
print(x - y)
print(x * y)
print(Fraction('.25'))
print(Fraction('1.25'))
print(Fraction('.25') + Fraction('1.25'))

print((2.5).as_integer_ratio())
f = 2.5
z = Fraction(*f.as_integer_ratio())
print(z)
x = Fraction(1, 3)
print(x + z)
print(float(x))
print(float(z))
print(float(x + z))
print(17 / 6)
print(Fraction.from_float(1.75))
print(Fraction(*(1.75).as_integer_ratio()))

s = {c * 4 for c in 'spamham'}
print(s | {'mmmm', 'xxxx'})
print(s & {'mmmm', 'xxxx'})