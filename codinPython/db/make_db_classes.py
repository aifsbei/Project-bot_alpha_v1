import shelve
from Person import Person

homer = Person('homer', 35)
peter = Person('peter', 40)
db = shelve.open('people_db_classes_file')
db['homer'] = homer
db['peter'] = peter
db.close()