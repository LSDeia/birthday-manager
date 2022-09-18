import json
import datetime

f = open('birthday.json','r+')
data = json.load(f)
today = datetime.date.today()

def menu():
    x = input("0 -> Check Birthday\n1 -> Add Birthday\n--> ")
    if (x=="0"):
        string_to_date(data)
        search_birthday(data)
        return
    else:
        ask_birthday(data)

def ask_birthday(birthday_list):
    dict = {}
    firstname = input("Prénom: ")
    lastname = input("Nom: ")
    dob = input("Date de naissance: ")
    dict["firstname"] = firstname
    dict["lastname"] = lastname
    dict["dob"] = dob
    add_birthday(data, dict)

def add_birthday(birthday_list, new_bd):
    birthday_list.append(new_bd)
    save_modif(birthday_list)

def is_birthday(today, dob):
    if today.month == dob.month and today.day == dob.day:
        return True

def string_to_date(birthday_list):
    for i in birthday_list :
        i['dob'] = datetime.datetime.strptime(i['dob'],'%Y-%m-%d')

def search_birthday(birthday_list):
    found = False;
    for i in birthday_list :
        if is_birthday(today, i['dob']) :
            print('Aujourd\'hui c\'est l\'anniversaire de', i['firstname'], i['lastname'],'!')
            found = True;
    if found == False:
        print('Aucun anniversaire aujourd\'hui !')

def print_json(birthday_list):
    print(birthday_list)

def save_modif(data):
    with open('birthday.json', 'w') as f:
        json.dump(data, f)


menu()
print_json(data)
f.close

