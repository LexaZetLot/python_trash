import module1
module1.printer('Hello world!')
import module2
print(module2.__dict__.keys())
print(list(name for name in module2.__dict__ if not name.startswith('_')))