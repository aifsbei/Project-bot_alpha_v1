from users_db import Users
from admins_db import Admins
import sys
import run
#from login_screen import root
#import main
from not_portable_launcher import NotPortableLauncher
from constants import *


def login(ents, errlabel):
    username = ents[0].get()
    if username == '':
        errlabel.config(text='Please, enter your username')
        return
    password = ents[1].get()
    if password == '':
        errlabel.config(text='Please, enter your password')
        return
    users = Users()
    admins = Admins()
    if admins.find(username, password) is not None:
        errlabel.config(text='')
        set_next_process('admin_screen.py')
        set_username(username)
        sys.exit()
    elif users.find(username, password) is not None:
#        print('is OK')
        errlabel.config(text='')
#        run.current_user = username
###        NotPortableLauncher('main', 'main.py')()
#        run.set_next_process('main.py')
        set_next_process('main.py')
        set_username(username)
        sys.exit()
#        root.quit()
    else:
#        print('No such user')
        errlabel.config(text='No such user!')
        return
#    print(users.find(username, password))


def registration(ents, errlabel):
    username = ents[0].get()
    if username == '':
        errlabel.config(text='Please, enter your username')
        return
    password = ents[1].get()
    if password == '':
        errlabel.config(text='Please, enter your password')
        return
    confirm_password = ents[2].get()
    if password != confirm_password:
        errlabel.config(text="passwords doesn't match")
#        print('пароли не совпадают!')
        return
    else:
        users = Users()
        if users.is_unque(username):
            users.append_table(username, password)
            errlabel.config(text='')
#            run.current_user = username
###            NotPortableLauncher('main', 'main.py')()
#            run.set_next_process('main.py')
            set_next_process('main.py')
            set_username(username)
            sys.exit()
#            root.quit()
        else:
            errlabel.config(text="this user is already exists")
            return


if __name__ == '__main__':
    login('something', 'else')