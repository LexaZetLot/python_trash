import shelve

db = shelve.open('persondb')
print(len(db))

print(list(db.keys()))
bob = db['Bob Smith']
print(bob)
print(bob.lastName())

for key in db:
    print(key, db[key])

for key in sorted(db):
    print(key, db[key])