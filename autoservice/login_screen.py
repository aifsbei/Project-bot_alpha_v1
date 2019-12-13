from tkinter import *
import PIL.Image, PIL.ImageTk
from constants import *
import lsc
######CONSTANTS######
fields = 'username', 'password'
register_fields = 'username', 'password', 'confirm password'


def make_entries(parent, iterable, bg):
    entries = []
    for iter in iterable:
        row = Frame(parent, bg=bg)
        lab = Label(row, bg=bg, fg=forecolor, width=15, text=iter + ': ')
        ent = Entry(row)
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT, padx=pad, pady=pad)
        ent.pack(side=RIGHT, expand=YES, fill=X, padx=pad, pady=pad)
        entries.append(ent)
    return entries


def create_top_side(parent):
    global render
    top_side = Frame(parent, bg=backgroundcolor)
    top_side.pack(side=TOP, fill=X)
    img = PIL.Image.open('logo2.png')
    render = PIL.ImageTk.PhotoImage(img)
    image = Label(top_side, image=render, bg=backgroundcolor).pack(side=LEFT, padx=pad, pady=pad)
    Label(top_side, text='+7(902)237-87-42\n+7(910)003-68-67',
          bg=backgroundcolor, fg=forecolor, font='times 12').pack(side=RIGHT, padx=pad, pady=pad)



def create_right_side(parent):
    right_side = Frame(parent, borderwidth=1, relief=RAISED, bg=backgroundcolor)
    right_side.pack(side=RIGHT, fill=BOTH)
    right_sign = Label(right_side, text='Register', fg=forecolor, bg=backgroundcolor,
                       font=("Helvetica", 16, "bold")).pack(side=TOP, fill=X, padx=pad, pady=pad)
    right_ents = make_entries(right_side, register_fields, backgroundcolor)
    right_ents[1].config(show=bullet)
    right_ents[2].config(show=bullet)
    right_status = Label(right_side, text='', fg='red2', bg=backgroundcolor, font=('times 12'))
    right_sign_btn = Button(right_side, text='SIGN UP', bg=backgroundcolor, fg=forecolor,
                            command=lambda: lsc.registration(right_ents, right_status)).pack(side=BOTTOM, padx=pad,
                                                                                             pady=pad)
    right_status.pack(side=BOTTOM, fill=X, padx=pad, pady=pad)


def create_left_side(parent):
    left_side = Frame(parent, borderwidth=1, relief=RAISED, bg=backgroundcolor)
    left_side.pack(side=LEFT, fill=BOTH)
    left_sign = Label(left_side, text='Login', fg=forecolor, bg=backgroundcolor, font=("Helvetica", 16, "bold")).pack(
        side=TOP, fill=X, padx=pad, pady=pad)
    left_ents = make_entries(left_side, fields, backgroundcolor)
    left_ents[1].config(show=bullet)
    left_status = Label(left_side, text='', fg='red', bg=backgroundcolor, font=('times 12'))
    left_sign_btn = Button(left_side, text='SIGN IN', bg=backgroundcolor, fg=forecolor,
                           command=lambda: lsc.login(left_ents, left_status)).pack(side=BOTTOM, padx=pad, pady=pad)
    left_status.pack(side=BOTTOM, fill=X, padx=pad, pady=pad)

if __name__ == '__main__':

    root = Tk()
    root.config(bg=backgroundcolor)
    root.resizable(False, False)
    root.title('Login Screen')

    create_top_side(root)

    create_right_side(root)

    create_left_side(root)

    root.mainloop()