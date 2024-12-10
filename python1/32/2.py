class MyList(list):
    my_list = []
    def __init__(self, init_list):
        super().__init__()
        self.my_list = init_list
    def __add__(self, other):
        return self.my_list + other.my_list
    def __getitem__(self, item):
        return self.my_list[item]
    def __iter__(self):
        return self.copy()
    def __next__(self):
        if self.my_list:
            return self.my_list.pop(0)
        else:
            raise StopIteration
    def append(self, item):
        self.my_list.append(item)
    def extend(self, other):
        self.my_list.extend(other)
        return self
    def sort(self):
        self.my_list.sort()
        return self
    def __str__(self):
        return str(self.my_list)
    def __repr__(self):
        return str(self.my_list)

X = MyList([1, 2, 3])
Y = MyList([4, 5, 6])
X = X + Y
G = iter(X)
print(next(G))
print(next(G))
print(next(G))
print(next(G))