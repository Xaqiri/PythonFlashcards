from controllers.deck_controller import DeckController
from models.user import User 
from mysql.connector import Error
from sqlite3 import Error as sqlite_error
import time

class UserController:
    
    def __init__(self, db):
        self._cur_user = None
        self.db = db
        self.connection = db.connection
        self.cur = db.cur
    
    @property
    def cur_user(self):
        return self._cur_user
    
    @cur_user.setter
    def cur_user(self, cur_user):
        self._cur_user = cur_user
    
    def get_user_info(self) -> User:
        ''' Helper function to get input '''
        name = input('Username: ')
        password = input('Password: ')
        user = User(name, password)
        return user
        
    def create_user(self) -> str:
        """Creates a new user and saves it to the database

        Returns:
            str: Status indicating success or failre
        """
        new_user = self.get_user_info()
        sql = f"INSERT INTO users (userId, name, password) VALUES (\'{new_user.id}\', \'{new_user.user_name}\', \'{new_user.password}\')"
        try:
            self.cur.execute(sql)
            self.connection.commit()
            print(self.cur.rowcount, "record inserted")
            self.db.user_cache += [(new_user.id, new_user.user_name)]
            return 'user_created'
        except Error as e:
            return 'user_found'
        except Exception as e:
            return 'user_found'
        
    def display_users(self):
        """Displays all users in the database
        """
        try:
            if len(self.db.user_cache) == 0:
                print('Connecting to database....')
                sql = "SELECT userId, name FROM users ORDER BY userId"
                self.cur.execute(sql)
                self.db.user_cache += [i for i in self.cur if i not in self.db.user_cache]
                time.sleep(0.5)
        except Error as e:
            print(e)
        [print(i) for i in self.db.user_cache]
            
    def update_user_name(self) -> str:
        """Updates the active user's name and saves it to the database

        Returns:
            str: Status indication success or failure
        """
        try:
            new_name = input('Enter new username: ')
            if len(new_name) == 0:
                return 'invalid_name'
            else:
                self.db.update_user_cache(self._cur_user, new_name, action='PUTS')
                self._cur_user.user_name = new_name
                self.cur.execute(f'UPDATE users SET name = \'{new_name}\' WHERE userId = \'{self._cur_user.id}\'')
                self.connection.commit()
                self._cur_user.user_name = new_name
                return 'user_updated'
        except Error as e:
            print(e)
            
    def delete_user(self, deck_controller, card_controller) -> str:
        """Deletes a user from the database if it exists

        Args:
            deck_controller (DeckController): Controller that handles deck operations
            card_controller (CardController): Controller that handles card operations

        Returns:
            str: Status indicating success or failure
        """
        choice = input('Are you sure? y/n ').casefold()
        if choice == 'y':
            try:
                deck_controller.delete_all_deck(deck_controller.cur_user.id, card_controller)
                self.cur.execute(f'DELETE FROM users WHERE userId = \'{self._cur_user.id}\'')
                self.connection.commit()
                self.db.update_user_cache(self._cur_user, action='DELETE')
                self._cur_user = None
                return 'user_deleted'
            except Error as e:
                print(e)
            except sqlite_error as err:
                print(err)
    
    def sign_in(self, deck) -> str:
        """Sign in to a user if it exists in the database and the password is correct

        Args:
            deck (DeckController): Controller that handles deck operations

        Returns:
            str: Status indicating success or failure
        """
        check_user = self.get_user_info()
        try:
            self.cur.execute(f'SELECT userId, name, password FROM users WHERE name = \'{check_user.user_name}\'')
            row = self.cur.fetchone()
        except Exception as e:
            print(e)
            return 'invalid_choice'
        if row is None:
            return 'user_not_found'
        else:
            if check_user.password != row[2]:
                return 'invalid_password'
            else:
                self._cur_user = User(id=row[0], user_name=row[1], password=row[2])
                deck.cur_user = self._cur_user
                return 'use_user'

    def sign_out(self, deck: DeckController):
        """Signs out of the current user and clears the cache

        Args:
            deck (DeckController): Controller that handles deck operations
        """
        self._cur_user = None
        deck.cur_deck = None
        self.db.deck_cache = []
        self.db.card_cache = []
