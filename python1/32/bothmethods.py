
class Methods:
    def imeth(self, x):
        print([self, x])

    def smeth(x):
        print([x])

    def cmeth(cls, x):
        print([cls, x])

    smeth = staticmethod(smeth)
    cmeth = classmethod(cmeth)