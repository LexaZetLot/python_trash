class Adder:
    def add(self, x, y):
        return 'Not Implemented'
class ListAdder(Adder):
    def add(self, x, y):
        return [x, y]
class DictAdder(Adder):
    def add(self, x, y):
        return {'1': x, '2': y}

X = ListAdder()
Y = DictAdder()
print(X.add(1, 2))
print(Y.add(1, 2))