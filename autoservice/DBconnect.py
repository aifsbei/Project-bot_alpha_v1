import psycopg2
from constants import get_db_name, get_db_user, get_db_password

#######VARIABLES#######
conn = None
cursor = None
#######################


def connect():
    global cursor, conn
    conn = psycopg2.connect(dbname=get_db_name(), user=get_db_user(), password=get_db_password())
    cursor = conn.cursor()


def disconnect():
    global cursor, conn
    cursor.close()
    conn.close()


if __name__ == '__main__':
    connect()
#    append_table('user1', 'easyPassword')
#    print(get_text())
    disconnect()