from autoservice_location_db import Autoservice_location
from services_db import Services
from users_db import Users
from clients_db import Clients
from cars_db import Cars
from workers_db import Workers
from tkinter import ttk
from tkinter import *
from tkinter.messagebox import askyesno, showerror
from constants import *
from main import set_profile_dialog_negative, set_profile_dialog_positive


def get_workers_data():
    workers = Workers()
    autoservice = Autoservice_location()
    autoservice_id = autoservice.get_autoservice_id(get_city(), get_address())
    return workers.get_workers(autoservice_id)


def set_cars_combobox(combo, username):
    cars_list = get_cars(username)
#    reformated_cars_list = [cell[0] + " - " + cell[2] + cell[3] for cell in cars_list]
#    combo['values'] = ([cell[0] + " - " + cell[2] + " " + cell[3] for value in cars_list for cell in value])
    combo['values'] = ([cell[0] + " - " + cell[2] + " " + cell[3] for cell in cars_list])


def remove_car(registration_plate):
    cars = Cars()
    cars.remove_car(registration_plate)


def get_cars(username):
    cars = Cars()
    users = Users()
    client_id = users.get_client_id(username)
    if client_id is None:
        return []
    list_of_cars = cars.get_cars(client_id)
    return list_of_cars


def add_car(car_info, username):
    users = Users()
    client_id = users.get_client_id(username)
    car = Cars()
    car.append_table(car_info[0].get(), car_info[1].get(),
                     car_info[2].get(), car_info[3].get(),
                     car_info[4].get(), client_id)


def get_clientdata():
    users = Users()
    client_id = users.get_client_id(get_username())
    clients = Clients()
    userdata = clients.get_userdata(client_id)
    return userdata


def set_clientdata(clientdata):
    clients = Clients()
    clients.append_table(clientdata[0].get(),
                         clientdata[1].get(),
                         clientdata[2].get(),
                         clientdata[3].get(),
                         clientdata[4].get())
    users = Users()
    users.update_fk_client_id(clients.get_max_id(), get_username())


def restore_clientdata(call_number):
    clients = Clients()
    try:
        id_clients = clients.search_by_callnumber(call_number)[0]
    except TypeError:
        showerror('No such user', 'No user with this call phone! Try again.')
        set_profile_dialog_positive()
        return
    users = Users()
    users.update_fk_client_id(id_clients, get_username())


def on_profile_open():
    users = Users()
    usname = "'" + get_username() + "'"
    if not users.has_visited(usname):
        ans = askyesno('Confirm yourself', 'Have you already visited our Autoservice?')
    else:
        return
    if ans:
        set_profile_dialog_positive()
    else:
        set_profile_dialog_negative()


def set_cities_combobox(combobox):
    autoservice = Autoservice_location()
    cities = autoservice.get_cities()
    city_list = []
    for city in cities:
        city_list.append(city[0])
    combobox['values'] = ([value for value in city_list])


def set_address_combobox(combobox, city):
    city = "'" + city + "'"
    autoservice = Autoservice_location()
#    print('city={}'.format(city))
    addresses = autoservice.get_address_via_city(city)
    address_list = []
    for address in addresses:
        address_list.append(address[2] + ', ' + address[3])
    combobox['values'] = ([value for value in address_list])


def set_services_treeview(treeview):
    services = Services().get_text()
    services_list = []
    for service in services:
        treeview.insert('', 'end', values=[item for item in service])


if __name__ == '__main__':
    print(get_cars(9))
