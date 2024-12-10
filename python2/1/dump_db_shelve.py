import shelve
db = shelve.open('people-shelve')
for key in db:
    print(key, '=>', db[key])
print(db['sue']['name'])
db.close()