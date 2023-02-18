'''
TODO: Add study options
TODO: Make the ui prettier
TODO: Encrypt passwords before saving to the database
TODO: Pull all of the sql queries out of the files they're in now and put them in globals, probably as a dict
TODO: Might be a good idea to put the controllers there too
BUG: Creating any entity before querying the database 
     prevents the cache from populating with the rest of the items on the database
BUG: Editing user name or deck name after creation allows you to bypass the unique constraint
     This only affects the cache for user name, but changes the deck name in the database as well
'''

from controllers.user_controller import UserController
from controllers.deck_controller import DeckController
from controllers.card_controller import CardController
from controllers.handle_status import handle_status
from views.main_menu import main_menu
from views.user_menu import user_menu
from views.deck_menu import deck_menu
from views.display_message import display_message
from database import Database
import os


def main():
    done: bool = False
    status: str = None
    DB: Database = Database()
    if DB.connection is None:
        done = True
    else:
        controllers = {
            'user': UserController(DB),
            'deck': DeckController(DB),
            'card': CardController(DB)
        }
    
    while not done:
        if status == 'exit':
            done = True
            break
        elif status is not None:
            status = handle_status(status, controllers)
            display_message(status)
        if controllers.get('deck').cur_deck is not None:
            print(f"Viewing deck: {controllers.get('deck').cur_deck.deck_name}")
            status = deck_menu()
        elif controllers.get('user').cur_user is not None:
            print(f"Logged in as: {controllers.get('user').cur_user.user_name}")
            status = user_menu()
        else:
            status = main_menu()
            
        os.system('clear')
    DB.close()
            
main()