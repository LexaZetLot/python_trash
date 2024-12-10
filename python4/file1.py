from cmath import sqrt

from matplotlib import pyplot as plt

X1 = -5
X2 = 5
f = 1
L = []

for Z in range(10, 1000):
    x1 = (-(X1 * f) / Z)
    x2 = (-(X2 * f) / Z)
    L.append(sqrt((x1 - x2) ** 2))
plt.plot(L)
plt.show()
