from user import User
from deck import Deck
import os
import json
import requests

'''
TODO: Split this monolith up into multiple files
'''

db = {'admin': User('admin', 'admin')}

cur_user = None
choices = {
    -5: 'deck_exists',
    -4: 'user_exists',
    -3: 'invalid_password',
    -2: 'invalid_username',
    -1: 'nonnumber',
    0: 'invalid',
    1: 'user_created',
    2: 'signed_in',
    3: 'exit',
    4: 'show_all_users',
    5: 'deck_created',
    6: 'show_all_decks',
    99: 'http://localhost:8080/user/all'
}

def get_user_info():
    name = input('Username: ')
    password = input('Password: ')
    user = User(name, password)
    return user
    
def create_new_user():
    new_user = get_user_info()
    if new_user.getUserName() in db.keys():
        return -4
    else: 
        db[new_user.getUserName()] = new_user
        return 1

def sign_in():
    global cur_user
    check_user = get_user_info()
    if check_user.getUserName() not in db.keys():
        return -2
    else:
        user = db[check_user.getUserName()]
        if user.getPassword() != check_user.getPassword():
            return -3
        else:
            cur_user = user
            return 2

def display_users():
    [print(f'{db[i].getUserName()}, {db[i].getId()}') for i in db]

def display_main_menu(choice):
    print('1. Create new user')
    print('2. Sign in')
    print('3. Exit')
    print('4. Display users')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0:
            choice = 0
    except:
        choice = -1
    match choice:
        case 1:
            choice = create_new_user()
        case 2:
            choice = sign_in()
            # r = requests.get(choices[4])
            # print(json.dumps(r.json(), indent=2))
        case 3:
            choice = 3
        case 4:
            choice = 4
    return choice

def display_user_menu(choice):
    print('1. Create new deck')
    print('2. Display decks')
    print('3. Study deck')
    print('4. Sign out')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0:
            choice = 0
    except:
        choice = -1
    match choice: 
        case 1:
            choice = create_deck()
        case 2:
            choice = 6
        case 3:
            pass
        case 4:
            global cur_user
            cur_user = None
            choice = None
    return choice

def create_deck():
    deck_name = input('Deck name: ')
    if deck_name in cur_user.decks:
        return -5
    else:
        new_deck = Deck(deck_name, cur_user.getId())
        cur_user.decks[deck_name] = new_deck
        return 5

def display_decks():
    [print(f'{cur_user.decks[i].getDeckName()}, {cur_user.decks[i].getId()}') for i in cur_user.decks]

def display_message(choice):
    match choices[choice]:
        case 'nonnumber':
            print('Choice must be a number')
        case 'invalid':
            print('Invalid choice')
        case 'invalid_username':
            print('Invalid username')
        case 'invalid_password':
            print('Invalid password')
        case 'user_created':
            print('User created')
        case 'user_exists':
            print('User already exists')
        case 'show_all_users':
            display_users()
        case 'deck_created':
            print('Deck created')
        case 'deck_exists':
            print('Deck already exists with that name')
        case 'show_all_decks':
            display_decks()
        
def main():
    done = False
    choice = None
    while not done:
        if choice is not None:
            display_message(choice)
            if choices[choice] == 'exit':
                done = True
                break
        if cur_user is not None:
            print(f'Logged in as: {cur_user.getUserName()}')
            choice = display_user_menu(choice)
        else:
            choice = display_main_menu(choice)
        os.system('clear')
            
main()