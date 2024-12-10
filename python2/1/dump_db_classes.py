import shelve

db = shelve.open('class-shelve')
for key in db:
    print(key, db[key].name, db[key].pay)

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())