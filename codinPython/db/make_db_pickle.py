from initdata import db
import pickle
dbfile = open('people_file', 'wb')
pickle.dump(db, dbfile)
dbfile.close()
