import shelve
from tkinter import *
from tkinter.messagebox import showerror

file_name = 'class-shelve'
fieldnames = ('name', 'age')

def make_widgets():
    global entries
    window = Tk()
    window.title('These people')
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key', ) + fieldnames):
        lab = Label(form, text = label)
        ent = Entry(form)
        lab.grid(row = ix, column = 0)
        ent.grid(row = ix, column = 1)
        entries[label] = ent
    btn_fetch = Button(form, text='Fetch', command = (lambda: fetch()))
    btn_fetch.grid(row = 3, column = 0)
    btn_update = Button(form, text = 'Update', command = (lambda: update()))
    btn_update.grid(row = 3, column = 1)
    return window


def fetch():
    print('fetch!')
    key = entries['key'].get()
    try:
       record = db[key]
    except:
        showerror(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))


def update():
    key = entries['key'].get()
    if key in db:
        record = db[key]
    else:
        from Person import Person
        record = Person(name = '?', age = '?')
    for field in fieldnames:
        setattr(record, field, entries[field].get())
    db[key] = record


db = shelve.open(file_name)
window = make_widgets()
window.mainloop()
db.close()