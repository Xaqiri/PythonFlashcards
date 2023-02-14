from globals import *
from user_controller import UserController
from deck_controller import DeckController
import os
import json
import requests
from mysql.connector import connect, Error
from dotenv import load_dotenv


'''
TODO: Figure out a better way to deal with choices. Classes shouldn't return choice numbers.
'''


def display_main_menu(choice, user_controller, deck_controller):
    print('1. Create new user')
    print('2. Sign in')
    print('3. Exit')
    print('4. Display users')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0 or choice > 4:
            choice = 0
    except:
        choice = -1
    match choice:
        case 1:
            choice = user_controller.create_new_user()
        case 2:
            choice = user_controller.sign_in()
            deck_controller.setCurUser(user_controller.getCurUser())
            # r = requests.get(choices[4])
            # print(json.dumps(r.json(), indent=2))
        case 3:
            choice = 3
        case 4:
            choice = 4
    return choice

def display_user_menu(choice, user_controller, deck_controller):
    print('1. Create new deck')
    print('2. Display decks')
    print('3. Study deck')
    print('4. Sign out')
    print('5. Edit username')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0 or choice > 5:
            choice = 0
    except:
        choice = -1
    match choice: 
        case 1:
            choice = deck_controller.create_deck()
        case 2:
            choice = 6
        case 3:
            pass
        case 4:
            user_controller.signOut()
            choice = None
        case 5:
            user_controller.update_user_name()
    return choice


def display_message(choice, user_controller, deck_controller):
    if type(choice) != int:
        print(choice)
        return
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
        case 'user_does_not_exist':
            print('User does not exist')
        case 'show_all_users':
            user_controller.display_users()
        case 'deck_created':
            print('Deck created')
        case 'deck_exists':
            print('Deck already exists with that name')
        case 'show_all_decks':
            deck_controller.display_decks()
        
def main():
    done = False
    choice = None
    db = None
    load_dotenv()
    try:
        db = connect(
        host='containers-us-west-164.railway.app',
        port='5810',
        user=os.environ['dbuser'],
        password=os.environ['password'],
        database='railway'
    )
        user_controller = UserController(db)
        deck_controller = DeckController(user_controller.getCurUser())
    except Error as e:
        print(e)
        done = True
    
    
    while not done:
        if choice is not None:
            display_message(choice, user_controller, deck_controller)
            if type(choice) != int: 
                choice = 0
            if choices[choice] == 'exit':
                done = True
                break
        if user_controller.getCurUser() is not None:
            print(f'Logged in as: {user_controller.getCurUser().getUserName()}')
            choice = display_user_menu(choice, user_controller, deck_controller)
        else:
            choice = display_main_menu(choice, user_controller, deck_controller)
        os.system('clear')
    if db is not None:
        db.close()
            
main()