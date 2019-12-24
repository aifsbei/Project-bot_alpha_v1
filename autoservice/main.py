from tkinter import *
import tkinter.ttk as ttk
from constants import *
import mc
from login_screen import create_top_side, make_entries
import re
from tkinter.messagebox import showerror
from functools import partial
import random
import tkinter.messagebox


###constants###
personality_confirmed = False


def create_services_frame():
    global services_frame
    try:
        services_frame.destroy()
    except NameError:
        pass
    services_frame = Frame(f1)
    services_frame.config(bg=inner_background)
    Label(services_frame, text='This autoservice provides the\nfollowing services*:',
          bg=inner_background, fg=forecolor, font='times 14').pack(side=TOP)
    services_frame.pack(side=BOTTOM, padx=pad, pady=pad, fill=BOTH, expand=YES)
    create_services_treeview(services_frame)
    text = Message(services_frame, bg=inner_background, fg=forecolor, width=500, anchor=W)
    text.config(text='''*The cost of the not mentioned works (services) is calculated based on the norms of time recommended by the manufacturer and the cost per hour equal 1500 rubles''')
    text.pack(side=BOTTOM, fill=X, expand=YES, padx=pad, pady=pad)
    btn_confirm_service = Button(services_frame, text='Confirm', command=lambda: on_btn_confirm_service_click(tree))
    btn_confirm_service.pack(side=RIGHT, fill=X, padx=pad, pady=pad)


def create_services_treeview(parent):
    global tree_frame, tree
    tree_frame = Frame(parent, bg=inner_background)
    tree_frame.pack(side=TOP)
    scrollbar = Scrollbar(tree_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    tree = ttk.Treeview(tree_frame, height=10, yscrollcommand=scrollbar.set)
    tree.config(selectmode='browse')
    tree['columns'] = ('1', '2', '3')
    tree['show'] = 'headings'
    tree.column('1', width=50, anchor=W)
    tree.column('2', width=600, anchor=W)
    tree.column('3', width=70, anchor=W)
    tree.heading('1', text='id')
    tree.heading('2', text='Name')
    tree.heading('3', text='Cost')
    tree.pack(side=TOP)
    scrollbar.config(command=tree.yview)
    mc.set_services_treeview(tree)


def create_address_combo():

    def on_address_change(index, value, op):
        try:
            set_autoservice_address(address_box_value.get())
            services_frame.destroy()
        except NameError:
            pass
        create_services_frame()

    global address_box_value, address_box
    address_box_value = StringVar()
    address_box = ttk.Combobox(f1, textvariable=address_box_value, state='readonly')
    address_box.pack(side=TOP, padx=pad, pady=pad, fill=X)
    address_box.set('Select address...')
    address_box_value.trace('w', on_address_change)
    mc.set_address_combobox(address_box, city_box.get())


def on_btn_confirm_service_click(treeview):
    create_checkout_tab(f2)
    nb.tab(1, state='normal')
    nb.select(f2)
    print(treeview.item(tree.focus())['values'][0])
    set_service_id(str(treeview.item(tree.focus())['values'][0]))


def create_city_combo():

    def on_city_change(index, value, op):
        #    address_box_value.__del__()
        try:
            set_autoservice_city(city_box_value.get())
            address_box.destroy()
            services_frame.destroy()
        except NameError:
            pass
        create_address_combo()

    global city_box_value, city_box
    city_box_value = StringVar()
    city_box = ttk.Combobox(f1, textvariable=city_box_value, state='readonly')
    mc.set_cities_combobox(city_box)
    city_box.set('Select city...')
    city_box_value.trace('w', on_city_change)
    city_box.pack(side=TOP, padx=pad, pady=pad, fill=X)


def create_general_tab(frame):
    Label(frame, text='Choose your autoservice:',
          fg=forecolor, bg=inner_background,
          font='times 14').pack(side=TOP, fill=X, padx=pad, pady=pad)
    create_city_combo()


def create_profile_tab(parent):

    def update_clientdata():
        clientdata = mc.get_clientdata()
        for i, item in enumerate(values):
            item.set(clientdata[i + 1])

    def on_edit_btn_click():
        set_profile_dialog_negative()
        update_clientdata()

    def on_add_card_click():
        global card_frame
        mc.add_card(get_username())
        frame.destroy()
        create_profile_tab(parent)
        create_card_info()

    def create_card_info():
        card = mc.get_membership_card(get_username())
        level = None
        if card[1] < 10:
            level = 'Bronze'
        elif 10 < card[1] < 15:
            level = 'Silver'
        elif 15 < card[1] < 20:
            level = 'Gold'
        elif 20 < card[1] <= 25:
            level = 'Platinum'
        try:
            Label(card_frame, text='Your card level is: ' + level + '\nCurrent discount is ' + str(card[1]) + '%', bg=inner_background, fg=forecolor, font='times 14').pack(side=TOP, fill=X)
        except TclError:
            print('its k')
        Label(card_frame, text='You need spend ' + str(25000 - card[2] % 25000) + ' more roubles with your membership\ncard to improve your level', bg=inner_background, fg=forecolor, justify=LEFT).pack(anchor=NW, fill=Y)
        if card[3] is not None:
            Label(card_frame, text='last purchase: ' + str(card[3]), bg=inner_background, fg=forecolor).pack(anchor=NW, fill=Y)
        else:
            Label(card_frame, text='You haven`t got recent purchases yet', bg=inner_background, fg=forecolor).pack(anchor=NW, fill=Y)


    mc.on_profile_open()
    frame = Frame(parent, bg=inner_background)
    frame.pack(side=TOP, expand=YES, fill=BOTH, padx=pad, pady=pad)
    Label(frame, text='Your Profile data: ', bg=inner_background, fg=forecolor, font='times 14').pack(side=TOP)
    clientdata = mc.get_clientdata()
    print(clientdata)
    values = []
    for ix, field in enumerate(client_fields):
        value = StringVar()
        row = Frame(frame, bg=inner_background)
        row.pack(side=TOP, fill=X)
        Label(row, text=field, bg=inner_background, fg=forecolor).pack(side=LEFT)
        Label(row, bg=inner_background, fg=forecolor, textvariable=value).pack(side=RIGHT)
        value.set(clientdata[ix + 1])
        values.append(value)
    edit_btn = Button(frame, text='Edit', bg=inner_background, fg=forecolor, command=on_edit_btn_click)
    edit_btn.pack(anchor=SE, padx=pad, pady=pad, fill=X)
    card_frame = Frame(frame, bg=inner_background)
    card_frame.pack(side=TOP, fill=BOTH)
    if mc.get_membership_card(get_username()) is None:
        Label(card_frame, text='Sorry, but You haven`t got\n a Membership card yet!', bg=inner_background, fg=forecolor, font='times 12').pack(side=TOP, fill=X)
        add_cart = Button(card_frame, text='\u2795 Click here to Add membership card', bg=inner_background, fg=blue_fore, relief=RIDGE, bd=0, cursor='hand2', command=on_add_card_click)
        add_cart.pack(side=TOP)
    else:
        create_card_info()


def set_profile_dialog_negative():

    def on_btn_click():
        mc.set_clientdata(ent)
        win.quit()

    def make_dialog_entries(parent, iterable, bg):
        entries = []
        for iter in iterable:
            row = Frame(parent, bg=bg)
            lab = Label(row, bg=bg, fg=forecolor, width=15, text=iter + ': ')
            ent = LabeledEntry(row, label=iterable[iter])
            row.pack(side=TOP, fill=X)
            lab.pack(side=LEFT, padx=pad, pady=pad)
            ent.pack(side=RIGHT, expand=YES, fill=X, padx=pad, pady=pad)
            entries.append(ent)
        return entries

    win = Toplevel(bg=backgroundcolor)
    ent = make_dialog_entries(win, client_fields, backgroundcolor)
    btn = Button(win, text='Confirm', command=on_btn_click, bg=backgroundcolor, fg=forecolor)
    btn.pack(side=BOTTOM, fill=X, padx=pad, pady=pad)
    win.protocol('WM_DELETE_WINDOW', win.quit)
    win.focus_set()
    win.grab_set()
    center_obj(win)
    win.mainloop()
    win.destroy()


def set_profile_dialog_positive():

    def on_btn_click():
        mc.restore_clientdata(ent.get())
        win.quit()

    win = Toplevel(bg=backgroundcolor)
    Label(win, text='Enter your call number to find\n your personality in database:', bg=backgroundcolor, fg=forecolor).pack(side=TOP, padx=pad, pady=pad, fill=X)
    ent = LabeledEntry(win, label='+7(XXX)XXX-XX-XX')
    ent.pack(side=TOP, padx=pad, pady=pad, fill=X)
    btn = Button(win, text='Confirm', command=on_btn_click, bg=backgroundcolor, fg=forecolor)
    btn.pack(side=BOTTOM, fill=X, padx=pad, pady=pad)
    win.protocol('WM_DELETE_WINDOW', lambda: sys.exit())
    win.focus_set()
    win.grab_set()
    center_obj(win)
    win.mainloop()
    win.destroy()


def create_car_tab(frame):

    def on_add_car_btn_click():

        def make_dialog_entries(parent, iterable, bg):
            entries = []
            for iter in iterable:
                row = Frame(parent, bg=bg)
                lab = Label(row, bg=bg, fg=forecolor, width=15, text=iter + ': ')
                ent = LabeledEntry(row, label=iterable[iter])
                row.pack(side=TOP, fill=X)
                lab.pack(side=LEFT, padx=pad, pady=pad)
                ent.pack(side=RIGHT, expand=YES, fill=X, padx=pad, pady=pad)
                entries.append(ent)
            return entries

        def on_btn_click():
            mc.add_car(ent, get_username())
            create_checkout_tab(f2)
            win.quit()

        win = Toplevel(bg=backgroundcolor)
        ent = make_dialog_entries(win, car_fields, backgroundcolor)
        btn = Button(win, text='Confirm', command=on_btn_click, bg=backgroundcolor, fg=forecolor)
        btn.pack(side=BOTTOM, fill=X, padx=pad, pady=pad)
        win.protocol('WM_DELETE_WINDOW', win.quit)
        win.focus_set()
        win.grab_set()
        center_obj(win)
        win.mainloop()
        win.destroy()
        cars_frame.destroy()
        create_car_info()
#        f2.update()

    def create_car_info():

        def on_btn_del_car_click(btn):
            for index, it in enumerate(del_btns):
                if btn is it:
                    print('MATCH!11!')
                    mc.remove_car(cars_info[index][0])
                    cars_frame.destroy()
                    create_car_info()
            create_checkout_tab(f2)

        global cars_frame
        cars_info = mc.get_cars(get_username())
        cars_frame = Frame(frame)
        del_btns = []
        for car_number, car in enumerate(cars_info):
            miniframe = Frame(cars_frame, bg=inner_background)
            miniframe.pack(side=TOP, fill=X)
            Label(miniframe, text='Car #' + str(car_number + 1), bg=inner_background, fg=forecolor, font='times 12').pack(side=LEFT)
            btn_del_car = Button(miniframe, text='Click here to remove', bg=inner_background, fg=blue_fore, relief=RIDGE, bd=0, cursor='hand2')
            btn_del_car.config(command=partial(on_btn_del_car_click, btn_del_car), font=('times', 12, 'underline'))
            btn_del_car.pack(side=LEFT)
            del_btns.append(btn_del_car)
            for ix, item in enumerate(car_fields):
                row = Frame(cars_frame, bg=inner_background)
                row.pack(side=TOP, fill=X)
                Label(row, text=item + ': ', bg=inner_background, fg=forecolor).pack(side=LEFT, padx=pad * 4, fill=X)
                Label(row, text=car[ix], bg=inner_background, fg=forecolor).pack(side=RIGHT, padx=pad, fill=X)
        cars_frame.pack(side=TOP, fill=X)

    add_car_btn = Button(frame, text='Add car', bg=inner_background, fg=forecolor, command=on_add_car_btn_click)
    add_car_btn.pack(side=TOP, fill=X, padx=pad, pady=pad)
    create_car_info()


def create_checkout_tab(parent):

    def on_car_change(index, value, op):
        try:
            workers_frame.destroy()
        except NameError:
            pass
        create_workers_info(None)

    def create_car_box():
        global car_box_value, car_box, frame
        try:
            frame.destroy()
        except NameError:
            print('wtf?')
        frame = Frame(parent, bg=inner_background)
        frame.pack(side=TOP, expand=YES, fill=BOTH)
        car_box_value = StringVar()
        car_box = ttk.Combobox(frame, textvariable=car_box_value, state='readonly')
        mc.set_cars_combobox(car_box, get_username())
        Label(frame, text="Choose your car: ", bg=inner_background, fg=forecolor, font='times 14').pack(side=TOP, fill=X, padx=pad, pady=pad)
        car_box.set('Select your car...')
        car_box_value.trace('w', on_car_change)
        car_box.pack(side=TOP, padx=pad, pady=pad, fill=X)

    def on_change_worker_click():
        global worker_index, list_of_workers
#        win = Toplevel(bg=backgroundcolor)
#        Label(win, text='Select another worker: ', bg=backgroundcolor, fg=forecolor, font='times 14').pack(side=TOP, fill=X)
        prev_index = None
        while True:
            prev_index = worker_index
            worker_index = random.randint(0, len(list_of_workers) - 1)
            if worker_index != prev_index:
                break
        try:
            workers_frame.destroy()
        except NameError:
            pass
        create_workers_info(worker_index)

    def on_appoint_btn_click():
        global car_box_value, worker_index, current_worker_data
        number = car_box_value.get().split(' - ')[0]
        print(number)
        mc.appoint(number, current_worker_data[0])

    def create_workers_info(set_none_to_random):
        global workers_frame, worker_index, list_of_workers, current_worker_data
        workers_frame = Frame(frame, bg=inner_background)
        workers_frame.pack(side=TOP, fill=X, padx=pad, pady=pad)
        varlabel = Label(workers_frame, text="Your worker is: ", bg=inner_background, fg=forecolor, font='times 14', justify=LEFT)
        varlabel.pack(side=TOP, fill=X)
        try:
            list_of_workers = [value for value in mc.get_workers_data()]
        except IndexError:
            varlabel.config(text='No workers that could provide your service.\nPlease, change address. ')
            return
        if set_none_to_random is not None:
            worker_index = set_none_to_random
        else:
            try:
                worker_index = random.randint(0, len(list_of_workers) - 1)
            except ValueError:
                varlabel.config(text='No workers that could provide your service.\nPlease, change address. ')
                return
        current_worker_data = list_of_workers[worker_index]
        for ix, field in enumerate(worker_fields):
            row = Frame(workers_frame, bg=inner_background)
            row.pack(side=TOP, fill=X)
            Label(row, text=worker_fields[ix], bg=inner_background, fg=forecolor).pack(side=LEFT)
            Label(row, text=current_worker_data[ix + 1], bg=inner_background, fg=forecolor).pack(side=RIGHT)
        one_more_row = Frame(workers_frame, bg=inner_background)
        one_more_row.pack(side=TOP, fill=X)
        change_worker_btn = Button(one_more_row, text='Click here to change worker', bg=inner_background, fg=blue_fore, relief=RIDGE, bd=0, cursor='hand2')
        change_worker_btn.pack(side=RIGHT, fill=X, padx=pad, pady=pad)
        change_worker_btn.config(command=on_change_worker_click, font=('times', 12, 'underline'))
        Button(workers_frame, text='Confirm', bg=inner_background, fg=forecolor, command=on_appoint_btn_click).pack(anchor=SE, padx=pad, pady=pad)

    create_car_box()


if __name__ == '__main__':

    root = Tk()
    root.geometry('800x600')
    root.config(bg=backgroundcolor)
    root.resizable(False, False)
    root.title('Autoservice')

    set_style()

    create_top_side(root)

    nb = ttk.Notebook(root)
    nb.config()
    nb.pack(fill=BOTH, expand=YES, padx=pad, pady=pad)



    f1 = Frame(root, bg=inner_background)
    create_general_tab(f1)

    f2 = Frame(root, bg=inner_background)
    create_checkout_tab(f2)

    f3 = Frame(root, bg=inner_background)
    create_car_tab(f3)

    f4 = Frame(root, bg=inner_background)
    create_profile_tab(f4)

    nb.add(f1, text='General')
    nb.add(f2, text='Checkout')
    nb.tab(1, state='hidden')
#    nb.pageconfigure(f2, state=Tix.DISABLED)
    nb.add(f3, text='Your car')
    nb.add(f4, text='Profile')
    print()
    root.mainloop()