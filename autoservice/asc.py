from constants import *
from db_tools import DB_tools
from tkinter import *
from tkinter import messagebox
import DBconnect


def login(name, user, password):
    try:
        set_db_name(name)
        set_db_user(user)
        set_db_password(password)
        DBconnect.connect()
    except:
        messagebox.showerror(title='Error', message='Wrong username or password!')
        return 0
    return 1

def set_tablenames(listbox):
    names = DB_tools().get_tablenames()
    names = set(names)
    for name in names:
        listbox.insert(END, name[0])


def update_tree(treeview, query):
    try:
        data, column_names = DB_tools().execute(query)
    except:
        messagebox.showerror(title='Error', message='No such command!')
        return

    print(column_names)
    try:
        treeview['columns'] = column_names
        treeview['show'] = 'headings'
        for name in column_names:
            treeview.heading(name, text=name)
        for line in data:
            treeview.insert('', 'end', values=[item for item in line])
    except TypeError:
        treeview['columns'] = ('status', )
        treeview['show'] = 'headings'
        treeview.heading('status', text='status')
        treeview.insert('', 'end', values="EXECUTED")
        pass