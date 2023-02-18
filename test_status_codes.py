from globals import *
import unittest
# import main
from mock_files import mock_display_message, mock_user_menu
from views import main_menu, user_menu, deck_menu
from controllers.user_controller import UserController
from controllers.deck_controller import DeckController
from controllers.card_controller import CardController

# STATUS_CODES = status_codes.StatusCodes()
class TestCalc(unittest.TestCase):
    
    # def test_not_found(self):
    #     STATUS_CODES.not_found = 'user'
    #     self.assertEqual(STATUS_CODES.not_found, 'User not found')
    #     STATUS_CODES.not_found = 'deck'
    #     self.assertEqual(STATUS_CODES.not_found, 'Deck not found')
    #     STATUS_CODES.not_found = 'card'
    #     self.assertEqual(STATUS_CODES.not_found, 'Card not found')

    # def test_messages(self):
    #     mock_display_message.STATUS_CODES.not_found = 'user'
    #     STATUS_CODES.not_found = 'user'
    #     self.assertEqual(STATUS_CODES.not_found, 'User not found')
        # STATUS_CODES.not_found = 'user'
        # self.assertEqual(mock_display_message.mock(STATUS_CODES.not_found), 'User not found')
        # self.assertEqual(mock_display_message.mock(STATUS_CODES.found), 'There already exists a user with this username')
    #     self.assertEqual(mock_display_message.mock(STATUS_CODES.updated), 'User updated')
    #     self.assertEqual(mock_display_message.mock(STATUS_CODES.deleted), 'User deleted')

    def test_main_menu(self):
        status = main_menu.handle_choice(-4)
        self.assertEqual(status, 'invalid_choice') # check choice too low
        status = main_menu.handle_choice(10)
        self.assertEqual(status, 'invalid_choice') # check choice too high
        # status = main_menu.main_menu()
        # self.assertEqual(status, 'not_number') # check choice is string
        
        status = main_menu.handle_choice(0)
        self.assertEqual(status, 'exit_user')
        status = main_menu.handle_choice(1)
        self.assertEqual(status, 'create_user')
        status = main_menu.handle_choice(2)
        self.assertEqual(status, 'use_user')
        status = main_menu.handle_choice(3)
        self.assertEqual(status, 'display_all_user')
        
    def test_user_menu(self):
        status = user_menu.handle_choice(0)
        self.assertEqual(status, 'exit_deck')
        status = user_menu.handle_choice(1)
        self.assertEqual(status, 'create_deck')
        status = user_menu.handle_choice(2)
        self.assertEqual(status, 'use_deck')
        status = user_menu.handle_choice(3)
        self.assertEqual(status, 'display_all_deck')
        status = user_menu.handle_choice(4)
        self.assertEqual(status, 'delete_deck')
        status = user_menu.handle_choice(5)
        self.assertEqual(status, 'update_user')
        status = user_menu.handle_choice(6)
        self.assertEqual(status, 'delete_user')
        
        # self.assertEqual(STATUS_CODES.create, 'create_deck')
        # self.assertEqual(STATUS_CODES.create, 'create_deck')
        
    # def test_status_codes(self):
    #     STATUS_CODES.display_all = 'user'
    #     self.assertEqual(STATUS_CODES.display_all, 'display_all_user')
    #     self.assertEqual(CHOICES[4], 'display_all_user')
    #     STATUS_CODES.display_all = 'deck'
    #     self.assertEqual(STATUS_CODES.display_all, 'display_all_deck')
    #     self.assertEqual(STATUS_CODES.exit, 'exit')
    #     STATUS_CODES.found = 'user'
    #     self.assertEqual(STATUS_CODES.found, 'A user already exists with this name')
    #     STATUS_CODES.create = 'user'
    #     self.assertEqual(STATUS_CODES.create, 'New user created')
    #     STATUS_CODES.delete = 'user'
    #     self.assertEqual(STATUS_CODES.delete, 'User deleted')
    #     STATUS_CODES.update = 'user'
    #     self.assertEqual(STATUS_CODES.update, 'User updated')
        
        
if __name__ == '__main__':
    unittest.main()