from globals import *
from user_controller import UserController
from deck_controller import DeckController
import os
import json
import requests

'''
TODO: Figure out a better way to deal with choices. Classes shouldn't return choice numbers.
TODO: Use sqlite as db until the django backend is hosted, or just connect to the db hosted on Railway
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
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0 or choice > 4:
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
    return choice


def display_message(choice, user_controller, deck_controller):
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
    user_controller = UserController()
    deck_controller = DeckController(user_controller.getCurUser())
    while not done:
        if choice is not None:
            display_message(choice, user_controller, deck_controller)
            if choices[choice] == 'exit':
                done = True
                break
        if user_controller.getCurUser() is not None:
            print(f'Logged in as: {user_controller.getCurUser().getUserName()}')
            choice = display_user_menu(choice, user_controller, deck_controller)
        else:
            choice = display_main_menu(choice, user_controller, deck_controller)
        os.system('clear')
            
main()