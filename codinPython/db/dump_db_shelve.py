from initdata import db
import shelve

db = shelve.open('people_shelve_file')
for key in db:
    print(db[key])