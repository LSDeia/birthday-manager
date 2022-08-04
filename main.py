import json
import datetime

f = open('birthday.json','r')
data = json.load(f)
today = datetime.date.today()

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

string_to_date(data)
search_birthday(data)
