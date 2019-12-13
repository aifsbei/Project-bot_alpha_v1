from constants import *
import tkinter.ttk as ttk
from tkinter import *
import asc


def create_window(parent):

    def create_listbox():
        global databases_listbox
        def popup(event):
            try:
                value = (databases_listbox.get(databases_listbox.curselection()))
                print(value)
            except TclError:
                pass

        def show_table(msg):
            table_tree.delete(*table_tree.get_children())
            try:
                value = (databases_listbox.get(databases_listbox.curselection()))
                msg.set('select * from {}'.format(value))
                exec_btn_on_click()
            except TclError:
                pass

        def insert_into_table():
            try:
                value = (databases_listbox.get(databases_listbox.curselection()))
                print(value)
            except TclError:
                pass

        databases_listbox = Listbox(parent, bg=inner_background, fg=forecolor, font='times 14')
        databases_listbox.pack(side=LEFT, padx=pad, pady=pad, fill=Y)
        asc.set_tablenames(databases_listbox)
#        print(asc.set_tablenames(databases_listbox))
        popup_menu = Menu(databases_listbox, tearoff=0)
        popup_menu.add_command(label='Show', command=lambda: show_table(query))
        popup_menu.add_command(label='Insert', command=lambda: insert_into_table())
        databases_listbox.bind("<Button-3>", lambda event: popup_menu.post(event.x_root, event.y_root))
        databases_listbox.bind("<Double-Button-1>", lambda event: show_table(query))

    def create_tree(frame):
        global table_tree
        tree_frame = Frame(frame)
        tree_frame.pack(side=TOP, expand=YES, fill=BOTH)
        table_tree = ttk.Treeview(tree_frame)
        vertical_sb = Scrollbar(tree_frame, orient='vertical', command=table_tree.yview)
        vertical_sb.pack(side=RIGHT, fill=Y)
        table_tree.pack(side=TOP, fill=BOTH, expand=YES)
        table_tree.configure(yscrollcommand=vertical_sb.set)
        horizontal_sb = Scrollbar(tree_frame, orient='horizontal', command=table_tree.xview)
        horizontal_sb.pack(side=BOTTOM, fill=X)
        table_tree.configure(xscrollcommand=horizontal_sb.set)
#        asc.update_tree(table_tree, 'select * from workers')
        return table_tree

    def exec_btn_on_click():
        table_tree.delete(*table_tree.get_children())
        asc.update_tree(table_tree, query.get())
        databases_listbox.delete(0, END)
        asc.set_tablenames(databases_listbox)

    global query_string, query
    query_frame = Frame(parent, bg=backgroundcolor)
    query = StringVar()
    query_string = Entry(query_frame, textvariable=query)
    create_listbox()
    query_frame.pack(side=RIGHT, padx=pad, pady=pad, fill=BOTH, expand=YES)
    table_tree = create_tree(query_frame)
    query_string.pack(side=LEFT, fill=X, expand=YES)
    exec_btn = Button(query_frame, text='Execute', bg=backgroundcolor, fg=forecolor, command=exec_btn_on_click)
    exec_btn.pack(side=RIGHT)


def create_login_dialog(parent):

    def on_btn_click():
        if asc.login(ents[0].get(), ents[1].get(), ents[2].get()):
            window.quit()

    def create_ents():
        ents = []
        for field in db_fields:
            row = Frame(window, bg=backgroundcolor)
            row.pack(side=TOP, fill=X)
            Label(row, text=field, bg=backgroundcolor, fg=forecolor).pack(side=LEFT, padx=pad, pady=pad)
            ent = Entry(row)
            ent.pack(side=RIGHT, fill=X, padx=pad, pady=pad)
            ents.append(ent)
        try:
            ents[0].insert(0, get_db_name())
            ents[0].config(bg=google_autofill_color)
            ents[0].bind('<Key>', lambda event: ents[0].config(bg='snow'))
            ents[1].insert(1, get_db_user())
            ents[1].config(bg=google_autofill_color)
            ents[1].bind('<Key>', lambda event: ents[0].config(bg='snow'))
            ents[2].focus_set()
        except IndexError:
            pass
        ents[2].config(show=bullet)
        return ents

    window = Toplevel(parent, bg=backgroundcolor)
    window.protocol('WM_DELETE_WINDOW', on_btn_click)
    center_obj(window)
    window.resizable(False, False)
    window.focus_set()
    window.grab_set()
    window.transient(parent)
    Label(window, text='Authorization', font='times 14', bg=backgroundcolor, fg=forecolor).pack(side=TOP, fill=X)
    ents = create_ents()
    Button(window, text='Confirm', bg=backgroundcolor, fg=forecolor, command=on_btn_click).pack(anchor=SE, padx=pad, pady=pad)
    window.mainloop()
    window.destroy()



if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    root.config(bg=backgroundcolor)
    root.resizable(False, False)
    root.title('SQL-Admin')
    create_login_dialog(root)
    create_window(root)
    root.mainloop()