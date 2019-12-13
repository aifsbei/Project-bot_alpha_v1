import shelve
from initdata import peter, homer

db = shelve.open('people_shelve_file')
db['homer'] = homer
db['peter']= peter
db.close()