class Animal:
    def speak(self):
        print('sound')
    def reply(self):
        self.speak()

class Manal(Animal):
    def speak(self):
        print('speak')

class Cat(Manal):
    def speak(self):
        print('may')

class Dog(Manal):
    def speak(self):
        print('gaf')

class Primate(Manal):
    def speak(self):
        print('prim')

class Hacker(Primate):
    def speak(self):
        print('hacker')

spot = Cat()
spot.reply()

data = Hacker()
data.reply()