import sys
import docstrings

print(dir(sys))
print(dir([]))

print(docstrings.square(10))
print(docstrings.__doc__)
print(docstrings.square.__doc__)
print(docstrings.Employee.__doc__)


help(sys.getrefcount)