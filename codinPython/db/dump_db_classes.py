import shelve

db = shelve.open('people_db_classes_file')
for key in db:
    print(db[key])