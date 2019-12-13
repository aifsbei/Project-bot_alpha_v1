import DBconnect


class Clients:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO clients(name, surname, patronymic, call_number, email) VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM clients')
        row = DBconnect.cursor.fetchall()
        return row

    def get_max_id(self):
        row = self.get_text()
        return row[-1][0]

    def get_userdata(self, client_id):
        value = "'" + str(client_id) + "'"
        DBconnect.cursor.execute('SELECT * FROM clients WHERE client_id=' + value + ';')
        row = DBconnect.cursor.fetchone()
        return row

    def search_by_callnumber(self, call_number):
        value = "'" + call_number + "'"
        DBconnect.cursor.execute('SELECT * FROM clients WHERE call_number=' + value + ';')
        row = DBconnect.cursor.fetchone()
        return row