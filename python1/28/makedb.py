import shelve
from person import Person, Manager

bob = Person('Bob Smith')
sue = Person('Sur Jones', job='dev', pay=1000)
tom = Manager('Tom Jones', 500)

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()