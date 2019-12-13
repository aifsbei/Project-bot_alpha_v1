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
