import DBconnect


class Membership_cards:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

    def append_table(self, *args):
        DBconnect.cursor.execute('INSERT INTO membership_cards VALUES ' + str(tuple(value for value in args)))
        DBconnect.conn.commit()

    def get_text(self):
        DBconnect.cursor.execute('SELECT * FROM membership_cards')
        row = DBconnect.cursor.fetchall()
        return row

    def find_my_card(self, client_id):
        client_id = str(client_id)
        DBconnect.cursor.execute('SELECT * FROM membership_cards where fk_client_id = ' + client_id)
        row = DBconnect.cursor.fetchone()
        return row

    def add(self, client_id, date):
        client_id = str(client_id)
        print(client_id)
        date = "'" + date + "'"
        DBconnect.cursor.execute("INSERT INTO membership_cards VALUES (default, 5, 0, NULL, {}, {})".format(date, client_id))
        DBconnect.conn.commit()