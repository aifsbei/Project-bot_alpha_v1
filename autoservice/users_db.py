import DBconnect


class Users:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO users VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def is_unque(self, *args):
        global cursor, conn
        username = "'" + args[0] + "'"
        DBconnect.cursor.execute('SELECT username FROM users WHERE username=' + username + ';')
        row = DBconnect.cursor.fetchone()
        if row is None:
            return True
        else:
            return False

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM users')
        row = DBconnect.cursor.fetchall()
        return row

    def has_visited(self, username):
        DBconnect.cursor.execute('SELECT fk_client_id FROM users WHERE username=' + username + ';')
        row = DBconnect.cursor.fetchone()
        print(row)
        if row[0] is None:
            return False
        else:
            return True

    def find(self, *args):
        un = "'" + args[0] + "'"
        pw = "'" + args[1] + "'"
        DBconnect.cursor.execute("SELECT * FROM users WHERE " + "username=" + un + " AND pass=" + pw + ";")
        row = DBconnect.cursor.fetchone()
        return row

    def update_fk_client_id(self, client_id, username):
        username = "'" + username + "'"
        DBconnect.cursor.execute('UPDATE users SET fk_client_id=' + str(client_id) + ' WHERE username=' + username + ';')
        DBconnect.conn.commit()

    def get_client_id(self, username):
        username = "'" + username + "'"
        DBconnect.cursor.execute('SELECT * FROM users WHERE username=' + username + ';')
        client_id = DBconnect.cursor.fetchone()[2]
        return client_id

if __name__ == '__main__':
    us = Users()
#    print(us.has_visited("'"'dan'"'"))
#    print(us.get_max_id())