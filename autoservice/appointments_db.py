import DBconnect

class Appointments:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO appointment VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM appointment')
        row = DBconnect.cursor.fetchall()
        return row

    def set(self, registration_plate, client_id, date, autoservice_id):
        registration_plate = "'" + registration_plate + "'"
        date = "'" + date + "'"
        DBconnect.cursor.execute('INSERT INTO appointment VALUES (default, {}, {}, {}, {})'.format(date, registration_plate, client_id, autoservice_id))
        DBconnect.conn.commit()