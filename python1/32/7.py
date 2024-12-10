class Lunch:
    def __init__(self):
        self.customer = Customer()
        self.employee = Employee()
    def order(self, foodName):
        self.customer.placeOrder(foodName, self.employee)
    def result(self):
        return str(self.customer.employee_init.food.name)
class Customer:
    def __init__(self):
        self.employee_init = Employee()
    def placeOrder(self, foodName, employee):
        self.employee_init = employee
        self.employee_init.takeOrder(foodName)
    def printFood(self):
        return str(self.employee_init.food.name)

class Employee:
    def __init__(self):
        self.food = None

    def takeOrder(self, foodName):
        self.food = Food(foodName)

class Food:
    def __init__(self, name):
        self.name = name

X = Lunch()
X.order('qwerty')
print(X.result())