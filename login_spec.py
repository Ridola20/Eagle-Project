from kivy.storage.jsonstore import JsonStore
from get_query import *

def login_configurations(ids, key):
    print("\nConfigurating.....\n")

    my_data = All(ids, key)

    store = JsonStore("DataBase/Do_Not_Delete.json")
    store.store_load()

    store.put("Login_Details", Id = f"{my_data[0]}", Name = f"{my_data[1]}", Classe = f"{my_data[3]}", Admission_number = f"{my_data[2]}", Passed_out = f'{my_data[6]}', Age = f"{my_data[4]}", Profile_image = f"{my_data[5]}", Key = f"{my_data[7]}", Gender = f"{my_data[8]}")

def login_configurations_admin(key):
    print("\nConfigurating.....\n")

    my_data = All_admin(key)

    store = JsonStore("DataBase/Do_Not_Delete2.json")
    store.store_load()

    store.put("Admin_Login_Details", Id = f"{my_data[0]}", Name = f"{my_data[1]}", position = f"{my_data[2]}", profile_image = f"{my_data[3]}", Key = f'{my_data[4]}')


def login_configurations_staff(ids, key):
    print("\nConfigurating.....\n")

    my_data = All_staff(ids, key)

    store = JsonStore("DataBase/Do_Not_Delete3.json")
    store.store_load()

    store.put("Staff_Login_Details", Id = f"{my_data[0]}", Name = f"{my_data[1]}", Positioin = f"{my_data[2]}", Profile_image = f"{my_data[3]}", Key = f'{my_data[4]}', Subjects = f"{my_data[5]}", Gender = f"{my_data[6]}", Staff_id = f"{my_data[7]}")
