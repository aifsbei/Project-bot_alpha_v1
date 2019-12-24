import tkinter as tk
from tkinter import ttk
import sys
import re
from tkinter import *
import datetime
from datetime import timedelta

makemodal = (len(sys.argv) > 1)
pad = 5
salt = 'j2h4k3ht9f230j'
bullet = '\u2022'
forecolor = 'white smoke'
blue_fore = 'dodger blue'
#backgroundcolor = 'LightSkyBlue4'
backgroundcolor = 'gray24'
inner_background = 'gray30'
google_autofill_color = '#FAFFBD'
client_fields = {'name': 'Should be capitalized',
          'surname': 'Should be capitalized',
          'patronymic': 'Should be capitalized',
          'call_number': '+7(XXX)XXX-XX-XX',
          'email': 'name@domain'}
car_fields = {'registration plate': 'Example: K897LM799',
              "owner's name": 'Full name',
              'make': 'Should be capitalized',
              'model': 'Should be capitalized',
              'VIN': '17 uppercase symbols, e.g.:1HGEG644387712345'}
worker_fields = ['specialization', 'name', 'surname', 'patronymic']
#db_list = ['admins', 'autoservice_location', 'cars', 'clients', 'services', 'users', 'workers']
db_fields = ['dbname', 'user', 'password']

def set_style():
    style = ttk.Style()
    settings = {"TNotebook": {"configure": {"background": "gray24"}},
        "TNotebook.Tab": {"configure": {"padding": [12, 4],
                                                "background": backgroundcolor
                                               },
                                  "map": {"background": [("selected", inner_background),
                                                         ("active", "gray10")],
                                          "foreground": [("selected", "#ffffff"),
                                                         ("active", "#ffffff")]

                                         }
                                  }
               }


#    style.theme_create("new_theme", parent="default", settings=settings)
    style.theme_use("default")

#    style.configure('Treeview.Item', foreground='red')
#    ttk.Style().configure('Treeview.Heading', fieldbackground=backgroundcolor, background='gray10', foreground=forecolor)
    style.configure('TNotebook', background=backgroundcolor)
    style.configure('TNotebook.Tab', padding=[12, 4])
    style.map('TNotebook.Tab', background=[('selected', inner_background),
                                           ('active', 'gray10'), ('disabled', 'gray50')], foreground=[('selected', '#ffffff'),
                                                                              ('active', '#ffffff')])
    style.configure('Treeview', fieldbackground=backgroundcolor, background=backgroundcolor, foreground=forecolor)


def get_username():
    f = open('temp.txt', 'r')
    rows = f.readlines()
    f.close()
    if rows[1][-1] == '\n':
        return rows[1][:-1]
    else:
        return rows[1]


def get_next_process():
    f = open('temp.txt', 'r')
    rows = f.readlines()
    f.close()
    if rows[0][-1] == '\n':
        return rows[0][:-1]
    else:
        return rows[0]


def set_username(username):
    f = open('temp.txt', 'r')
    rows = f.readlines()
    try:
        rows[1] = username
    except IndexError:
        rows.append(username)
    f.close()
    f = open('temp.txt', 'w')
    for item in rows:
        if item[-1] != '\n':
            item += '\n'
        f.write(item)
    f.close()


def set_next_process(next_process):
    f = open('temp.txt', 'r')
    rows = f.readlines()
    try:
        rows[0] = next_process
    except IndexError:
        rows.append(next_process)
    f.close()
    f = open('temp.txt', 'w')
    for item in rows:
        if item[-1] != '\n':
            item += '\n'
        f.write(item)
    f.close()


def set_autoservice_address(address):
    f = open('temp.txt', 'r')
    rows = f.readlines()
    try:
        rows[2] = address
    except IndexError:
        rows.append(address)
    f.close()
    f = open('temp.txt', 'w')
    for item in rows:
        if item[-1] != '\n':
            item += '\n'
        f.write(item)
    f.close()


def set_autoservice_city(city):
    f = open('temp.txt', 'r')
    rows = f.readlines()
    try:
        rows[3] = city
    except IndexError:
        rows.append(city)
    f.close()
    f = open('temp.txt', 'w')
    for item in rows:
        if item[-1] != '\n':
            item += '\n'
        f.write(item)
    f.close()


def get_city():
    f = open('temp.txt', 'r')
    rows = f.readlines()
    f.close()
    if rows[3][-1] == '\n':
        return rows[3][:-1]
    else:
        return rows[3]


def get_address():
    f = open('temp.txt', 'r')
    rows = f.readlines()
    f.close()
    if rows[2][-1] == '\n':
        return rows[2][:-1]
    else:
        return rows[2]


def set_db_name(name):
    f = open('temp.txt', 'r')
    rows = f.readlines()
    try:
        rows[4] = name
    except IndexError:
        rows.append(name)
    f.close()
    f = open('temp.txt', 'w')
    for item in rows:
        if item[-1] != '\n':
            item += '\n'
        f.write(item)
    f.close()


def set_db_user(user):
    f = open('temp.txt', 'r')
    rows = f.readlines()
    try:
        rows[5] = user
    except IndexError:
        rows.append(user)
    f.close()
    f = open('temp.txt', 'w')
    for item in rows:
        if item[-1] != '\n':
            item += '\n'
        f.write(item)
    f.close()


def set_db_password(password):
    f = open('temp.txt', 'r')
    rows = f.readlines()
    try:
        rows[6] = password
    except IndexError:
        rows.append(password)
    f.close()
    f = open('temp.txt', 'w')
    for item in rows:
        if item[-1] != '\n':
            item += '\n'
        f.write(item)
    f.close()


def get_db_name():
    f = open('temp.txt', 'r')
    rows = f.readlines()
    f.close()
    if rows[4][-1] == '\n':
        return rows[4][:-1]
    else:
        return rows[4]


def get_db_user():
    f = open('temp.txt', 'r')
    rows = f.readlines()
    f.close()
    if rows[5][-1] == '\n':
        return rows[5][:-1]
    else:
        return rows[5]


def get_db_password():
    f = open('temp.txt', 'r')
    rows = f.readlines()
    f.close()
    if rows[6][-1] == '\n':
        return rows[6][:-1]
    else:
        return rows[6]


def get_service_id():
    f = open('temp.txt', 'r')
    rows = f.readlines()
    f.close()
    if rows[7][-1] == '\n':
        return rows[7][:-1]
    else:
        return rows[7]


def set_service_id(service):
    f = open('temp.txt', 'r')
    rows = f.readlines()
    try:
        rows[7] = service
    except IndexError:
        rows.append(service)
    f.close()
    f = open('temp.txt', 'w')
    for item in rows:
        if item[-1] != '\n':
            item += '\n'
        f.write(item)
    f.close()

def get_date():
    d = datetime.date.today()
    return str(d.day) + '-' + str(d.month) + '-' + str(d.year)

def get_next_week_date():
    d = datetime.date.today()
    week = timedelta(7)
    d = d + week
    return str(d.day) + '-' + str(d.month) + '-' + str(d.year)


class LabeledEntry(tk.Entry):
    def __init__(self, master=None, label="Search", **kwargs):
        tk.Entry.__init__(self, master, **kwargs)
        self.label = label
        self.on_exit()
        self.bind('<FocusIn>', self.on_entry)
        self.bind('<FocusOut>', self.on_exit)

    def on_entry(self, event=None):
        if self.get() == self.label:
            self.delete(0, tk.END)
            self.config(fg='black')

    def on_exit(self, event=None):
        if not self.get():
            self.insert(0, self.label)
            self.config(fg='gray35')


class FancyListbox(Listbox):

    def __init__(self, parent, *args, **kwargs):
        Listbox.__init__(self, parent, *args, **kwargs)

        self.popup_menu = Menu(self, tearoff=0)
        self.popup_menu.add_command(label="Show",
                                    command=self.show_selected)
        self.popup_menu.add_command(label="Select All",
                                    command=self.select_all)

        self.bind("<Button-3>", self.popup) # Button-2 on Aqua
        self.entry = None
        self.button = None

    def popup(self, event):
        try:
            self.popup_menu.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup_menu.grab_release()

    def set_entry(self, entry):
        self.entry = entry

    def set_button(self, button):
        self.button = button

    def show_selected(self):
        for i in self.curselection()[::-1]:
            self.entry['text'] = 'NO'
            print('why?')

    def select_all(self):
        self.selection_set(0, 'end')


def center_obj(win):
    win.update_idletasks()

    w, h, sx, sy = map(int, re.split('x|\+', win.winfo_geometry()))
    sw = (win.winfo_rootx() - sx) * 2 + w
    sh = (win.winfo_rooty() - sy) + (win.winfo_rootx() - sx) + h
    sx = (win.winfo_screenwidth() - sw) // 2
    sy = (win.winfo_screenheight() - sh) // 2

    win.wm_geometry('+%d+%d' % (sx, sy))


if __name__ == '__main__':
#    set_next_process('login')
#    set_username('aifsbei')
#    get_next_process()
#    get_username()
    set_db_name('Autoservice')
    get_db_name()