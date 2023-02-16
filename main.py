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
TODO: Delete all decks associated with user when user is deleted
TODO: Delete all cards associated with deck wen deck is deleted
TODO: Update databases to add option to create and connect to a local sqlite database if a connection can not be made
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
        os.system('clear')
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
    db.close()
            
main()