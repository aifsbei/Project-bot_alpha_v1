import DBconnect


class Services:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO services VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM services')
        row = DBconnect.cursor.fetchall()
        return row

    def get_service_name_via_id(self, service_id):
        service_id = str(service_id)
        DBconnect.cursor.execute('SELECT * FROM services where id_service = ' + service_id)
        row = DBconnect.cursor.fetchone()
        return row[1]
