class Customer:
    def line(self):
        print("that's one ex-bird!")
class Clerk:
    def line(self):
        print("no it isn't")
class Parrot:
    def line(self):
        print("None")



class Scene():
    def __init__(self):
        self.parrot = Parrot()
        self.clerk = Clerk()
        self.customer = Customer()
    def action(self):
        self.parrot.line()
        self.clerk.line()
        self.customer.line()


x = Scene()
x.action()