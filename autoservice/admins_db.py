import DBconnect


class Admins:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO admins VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM admins')
        row = DBconnect.cursor.fetchall()
        return row

    def find(self, *args):
        un = "'" + args[0] + "'"
        pw = "'" + args[1] + "'"
        DBconnect.cursor.execute("SELECT * FROM admins WHERE " + "username=" + un + " AND pass=" + pw + ";")
        row = DBconnect.cursor.fetchone()
        return row