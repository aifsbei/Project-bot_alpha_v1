import DBconnect

class Orders:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO orders VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM orders')
        row = DBconnect.cursor.fetchall()
        return row

    def set(self, date, worker_id, service_id, registration_plate, client_id):
        registration_plate = "'" + registration_plate + "'"
        date = "'" + date + "'"
        print(date, worker_id, service_id, registration_plate, client_id)
        DBconnect.cursor.execute('INSERT INTO orders VALUES (default, {}, NULL,  {}, {}, {}, {})'.format(date, worker_id, service_id, registration_plate, client_id))
        DBconnect.conn.commit()