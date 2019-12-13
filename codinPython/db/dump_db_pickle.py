from initdata import db
import pickle
dbfile = open('people_file', 'rb')
db = pickle.load(dbfile)
for key in db:
    print(db[key])
