from user import User
import os
import json
import requests

db = {}
cur_user = None
choices = {
    0: 'invalid',
    1: 'create_user',
    2: 'sign_in',
    3: 'exit',
    4: 'http://localhost:8080/user/all'
}

def create_new_user(name, password):
    new_user = User(name, password)
    db[name] = new_user

def display_users():
    global cur_user
    [print(db[i]) for i in db.keys()]
    name = input('Username: ')
    password = input('Password: ')
    checkUser = User(name, password)
    if checkUser.getUserName() not in db.keys():
        print('Invalid username')
    else:
        user = db[name]
        if user.getPassword() != password:
            print('Invalid password')
        else:
            print('User logged in')
            cur_user = user
        
def display_menu(choice):
    if cur_user:
        print(f'Logged in as: {cur_user.getUserName()}')
    if choice not in choices:
        print('Choice must be a number')
    print('1. Create new user')
    print('2. Sign in')
    print('3. Exit')
    print('4: Test')
    choice = input().casefold()
    try:
        choice = int(choice)
        if choice not in choices.keys():
            choice = 'Invalid choice'
    except:
        choice = 0
    match choice:
        case 1:
            name = input('Name: ')
            password = input('Password: ')
            create_new_user(name, password)
        case 2:
            display_users()
        case 3:
            choice = 'exit'
        case 4:
            r = requests.get(choices[4])
            print(json.dumps(r.json(), indent=2))
        
    return choice

def main():
    done = False
    choice = ''
    while not done:
        choice = display_menu(choice)
        os.system('clear')
        if choice == 'exit':
            done = True
            
main()