import DBconnect


class Autoservice_location:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO autoservice_location VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM users')
        row = DBconnect.cursor.fetchall()
        return row

    def get_cities(self):
        DBconnect.cursor.execute('SELECT DISTINCT city FROM autoservice_location')
        row = DBconnect.cursor.fetchall()
        return row

    def get_address_via_city(self, city):
        DBconnect.cursor.execute('SELECT * FROM autoservice_location WHERE city=' + city + ';')
        row = DBconnect.cursor.fetchall()
        return row

    def get_autoservice_id(self, city, address):
        city = "'" + city + "'"
        street, building = address.split(', ')
        street = "'" + street + "'"
        building = "'" + building + "'"
        DBconnect.cursor.execute('SELECT * FROM autoservice_location WHERE city=' + city + ' AND street=' + street + ' AND building=' + building + ';')
        row = DBconnect.cursor.fetchone()
        return row[0]