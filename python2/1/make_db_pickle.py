from initdata import db
import pickle

dbfile = open('people-picle', 'wb')
pickle.dump(db, dbfile)
dbfile.close()