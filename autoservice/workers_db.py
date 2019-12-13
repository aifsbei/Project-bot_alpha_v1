import DBconnect

class Workers:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO workers VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM workers')
        row = DBconnect.cursor.fetchall()
        return row

    def get_workers(self, autoservice_id):
        DBconnect.cursor.execute('SELECT * FROM workers WHERE fk_autoservice_id=' + str(autoservice_id) + ';')
        rows = DBconnect.cursor.fetchall()
        return rows