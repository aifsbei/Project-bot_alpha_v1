import DBconnect

class Cars:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO cars VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM cars')
        row = DBconnect.cursor.fetchall()
        return row

    def get_cars(self, client_id):
        DBconnect.cursor.execute('SELECT * FROM cars WHERE fk_client_id=' + str(client_id) + ';')
        rows = DBconnect.cursor.fetchall()
        return rows

    def get_car(self, registration_plate):
        DBconnect.cursor.execute('SELECT * FROM cars WHERE registration_plate=' + registration_plate + ';')
        rows = DBconnect.cursor.fetchone()
        return rows

    def remove_car(self, registration_plate):
        registration_plate = "'" + registration_plate + "'"
        DBconnect.cursor.execute('DELETE FROM cars WHERE registration_plate=' + registration_plate + ';')
        DBconnect.conn.commit()