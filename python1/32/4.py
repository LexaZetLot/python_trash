class Attrs:
    def __getattr__(self, name):
        print(name)
    def __setattr__(self, name, value):
        print(name, value)

X = Attrs()
X.does
X.x = '12'
print(X.does)