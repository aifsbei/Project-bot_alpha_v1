from not_portable_launcher import NotPortableLauncher
import subprocess
from constants import *


current_user = None
#next_process = 'login_screen.py'


if __name__ == '__main__':
    set_db_name('Autoservice')
    set_db_user('postgres')
    set_db_password('F29cHZGh')
    set_next_process('login_screen.py')
#    next_process = set_next_process('login_screen.py')
    while True:
        next_process = get_next_process()
        if next_process == 'None':
            break
        else:
            p = subprocess.Popen([next_process], shell=True)
#        print(next_process)
#        next_process = ''
        set_next_process('None')
        p.wait()
#    print(next_process)