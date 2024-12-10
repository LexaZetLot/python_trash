from number import Number

num = Number(1)
num.add(4)
num.display()
num.sub(2)
num.display()

res = num.square()
print('square: ', res)

num.data = 99
val = num.data
print('data:   ', val)
print('data+1: ', val + 1)

num.display()
print(num)
del num