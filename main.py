from globals import *
from user_controller import UserController
from deck_controller import DeckController
from database import Database
import os


'''
TODO: Figure out a better way to deal with choices. Right now it works more like a status code
TODO: Move the menus to their own class
TODO: Add card class and CRUD operations
TODO: Add study options
TODO: Cache database calls
'''


def display_main_menu(choice, user_controller, deck_controller):
    print('0. Exit')
    print('1. Create new user')
    print('2. Sign in')
    print('3. Display users')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0 or choice > 4:
            choice = 0
    except:
        choice = -1
    match choice:
        case 0:
            choice = 3
        case 1:
            choice = user_controller.create_new_user()
        case 2:
            choice = user_controller.sign_in()
            deck_controller.cur_user = user_controller.cur_user
        case 3:
            # r = requests.get(choices[4])
            # print(json.dumps(r.json(), indent=2))
            choice = 4
    return choice

def display_user_menu(choice, user_controller, deck_controller):
    print('1. Create new deck')
    print('2. Study deck')
    print('3. Display decks')
    print('4. Update deck')
    print('5. Delete deck')
    print('6. Sign out')
    print('7. Edit username')
    print('8. Delete user')
    print('0: Exit')
    try:
        choice = int(input())
        if choice not in choices.keys() or choice < 0 or choice > 8:
            choice = 0
    except:
        choice = -1
    match choice: 
        case 0:
            choice = 3
        case 1:
            choice = deck_controller.create_deck()
        case 2:
            pass
        case 3:
            choice = 6
        case 4:
            inp = input('Enter deck name: ')
            choice = deck_controller.update_deck_name(inp)
        case 5:
            deckId = input('Enter deck id to delete: ').casefold()
            choice = deck_controller.delete_deck(deckId)
        case 6:
            user_controller.sign_out()
            choice = None
        case 7:
            choice = user_controller.update_user_name()
        case 8:
            inp = input('Are you sure? This action is irreversible  y/n ').casefold()
            if inp == 'y':
                choice = user_controller.delete_user()
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
        case 'user_deleted':
            print('User deleted')
        case 'deck_deleted':
            print('Deck deleted')
        case 'deck_not_found':
            print('Deck not found')
        case 'deck_name_updated':
            print('Deck name updated ')
        case 'user_name_updated':
            print('User name updated')
        
def main():
    done = False
    choice = None
    db = Database()
    if db.connection is None:
        done = True
    else:
        user_controller = UserController(db.connection)
        deck_controller = DeckController(db.connection)
    
    while not done:
        if choice is not None:
            display_message(choice, user_controller, deck_controller)
            if type(choice) != int: 
                choice = 0
            if choices[choice] == 'exit':
                done = True
                break
        if user_controller.cur_user is not None:
            print(f'Logged in as: {user_controller.cur_user.user_name}')
            choice = display_user_menu(choice, user_controller, deck_controller)
        else:
            choice = display_main_menu(choice, user_controller, deck_controller)
        os.system('clear')
    db.close()
            
main()