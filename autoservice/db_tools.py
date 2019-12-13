import DBconnect

class DB_tools:

    def __init__(self):
        DBconnect.connect()

    def __del__(self):
        DBconnect.disconnect()

#    @staticmethod
    def get_tablenames(self):
        DBconnect.cursor.execute("SELECT table_name FROM information_schema.columns where table_schema = 'public'")
        rows = DBconnect.cursor.fetchall()
        return rows

#    def get_columnnames(self, tablename):
#        tablename = "'" + tablename + "'"
#        DBconnect.cursor.execute("SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = " + tablename + ";")
#        rows = DBconnect.cursor.fetchall()
#        return rows

    def execute(self, query):
        DBconnect.cursor.execute(query)
        try:
            rows = DBconnect.cursor.fetchall()
            column_names = [name[0] for name in DBconnect.cursor.description]
            return rows, column_names
        except:
            DBconnect.conn.commit()
            return None, None


if __name__ == '__main__':
    print(DB_tools().execute('select * from cars'))