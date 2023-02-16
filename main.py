from globals import *
from controllers.user_controller import UserController
from controllers.deck_controller import DeckController
from controllers.card_controller import CardController
from views.main_menu import main_menu
from views.user_menu import user_menu
from views.deck_menu import deck_menu
from views.message import display_message
from database import Database

import os


'''
TODO: Split choices into two variables: choice and status
TODO: Add study options
TODO: Add comments
TODO: Make the ui prettier
TODO: Encrypt passwords before saving to the database
TODO: Pull all of the sql queries out of the files they're in now and put them in globals, probably as a dict
TODO: Might be a good idea to put the controllers there too
BUG: Creating any entity before querying the database 
     prevents the cache from populating with the rest of the items on the database
BUG: Editing user name or deck name after creation allows you to bypass the unique constraint
     This only affects the cache for user name, but changes the deck name in the database as well
'''


def main():
    done = False
    choice = None
    db = Database()
    if db.connection is None:
        done = True
    else:
        controllers = {
            'user': UserController(db),
            'deck': DeckController(db),
            'card': CardController(db)
        }
    
    while not done:
        if choice is not None:
            display_message(choice, db)
            if type(choice) != int: 
                choice = 0
            if choices[choice] == 'exit':
                done = True
                break
        if controllers.get('deck').cur_deck is not None:
            print(f"Viewing deck: {controllers.get('deck').cur_deck.deck_name}")
            choice = deck_menu(choice, controllers)
        elif controllers.get('user').cur_user is not None:
            print(f"Logged in as: {controllers.get('user').cur_user.user_name}")
            choice = user_menu(controllers)
        else:
            choice = main_menu(controllers)
        os.system('clear')
    db.close()
            
main()