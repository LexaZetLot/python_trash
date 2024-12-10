import pickle
dbfile = open('people-picle', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(key, '=>', db[key])
