import os
from mysql.connector import connect, Error
import sqlite3 
from dotenv import load_dotenv
import time
class Database:
    def __init__(self):
        self._type = None
        self._cur = None
        self._connection = None
        self.connect()
        self.user_cache = []
        self.deck_cache = []
        self.card_cache = []
        
    def connect(self):
        ''' 
        Connects to the database. Attempts to connect to the db
        with the parameters defined in .env first, and creates a 
        local sqlite db as a fallback
        '''
        load_dotenv()
        print('Connecting....')
        try:
            self._connection = connect(
            host=os.environ['host'],
            port=os.environ['port'],
            user=os.environ['user'],
            password=os.environ['password'],
            database=os.environ['db'],
            buffered=True
        )
        except KeyError as e:
            # Raises an error if the proper variables aren't in .env
            if not os.path.exists('flashcards.db'):
                print('Database not found. Create a .env file and store your variables there if you have a cloud database you want to use')
                print('Reverting to local database....')
                time.sleep(0.5)
        except Error as err:
            print(err)
        
        if self._connection is None:
            self.connect_local_db()
        else:
            self._type = 'mysql'
        
        try:
            self._cur = self._connection.cursor()
            self.make_tables()
        except Error as e:
            print(e)
        except Exception:
            print('Exiting....')
            time.sleep(0.5)
            
    @property
    def connection(self):
        return self._connection
    
    @connection.setter
    def connection(self, connection):
        self._connection = connection
        
    @property
    def cur(self):
        return self._cur
    
    @property
    def type(self):
        return self._type
    
    def connect_local_db(self):
        ''' 
            Connects to the local sqlite database
            and creates one if it doesn't exist
        '''
        if not os.path.exists('flashcards.db'):
            inp = input('Do you want to create a local database? ')
            if inp.casefold() != 'y':
                print('Database not created')
                time.sleep(0.5)
                return
            print('Connecting....')
            time.sleep(0.5)
        try:
            self._connection = sqlite3.connect('flashcards.db')
            self._connection.execute('pragma foreign_keys = on')
        except Error as e:
            print(e)
        self._type = 'sqlite'
        
    def make_tables(self):
        ''' 
        Creates the database tables: 
        users: userId, name, password
        decks: deckId, name, userId
        flashcards: cardId, front, back, deckId
        '''
        print(f'Database type: {self._type}')
        print('Checking tables....')
        time.sleep(0.5)
        try:
            self.make_table_users()
            self.make_table_decks()
            self.make_table_cards()
        except Error as e:
            print(e)
        except Exception as exc:
            print(exc)
            
    def make_table_users(self):
        ''' Create users table if it doesn't exist '''
        if self._type == 'sqlite':    
            sql = f'''
                    select name
                    from sqlite_master
                    where name = 'users'
                    '''
        else: 
            sql = 'show tables like "users"'
        try:
            self._cur.execute(sql)
            if self._type == 'mysql':
                exists = self._cur.rowcount != 0
            else:
                exists = len(self._cur.fetchall()) != 0
            if not exists:
                print('Making table users...')
                time.sleep(0.5)
                self._cur.execute('''
                                CREATE TABLE IF NOT EXISTS users (
                                userId varchar(50), 
                                name varchar(50) NOT NULL UNIQUE,
                                password varchar(20) NOT NULL, 
                                PRIMARY KEY (userId)
                                );'''
                            )
            else:
                print('Found users....')
                time.sleep(0.2)
        except Error as e:
            print(e)
        except Exception as exc:
            print(exc)
            
    def make_table_decks(self):
        ''' Create decks table if it doesn't exist '''
        if self._type == 'sqlite':    
            sql = f'''
                    select name
                    from sqlite_master
                    where name = 'decks'
                    '''
        else: 
            sql = 'show tables like "decks"'
        try:
            self._cur.execute(sql)
            if self._type == 'mysql':
                exists = self._cur.rowcount != 0
            else:
                exists = len(self._cur.fetchall()) != 0
            if not exists:
                print('Making table decks...')
                time.sleep(0.5)
                self._cur.execute('''
                                CREATE TABLE IF NOT EXISTS decks (
                                deckId varchar(50), 
                                name varchar(20) NOT NULL,
                                userId varchar(50), 
                                PRIMARY KEY (deckId), 
                                FOREIGN KEY (userId) REFERENCES users (userId)
                                ON DELETE CASCADE
                                );'''
                            )
            else:
                print('Found decks....')
                time.sleep(0.2)
        except Error as e:
            print(e)
        except Exception as exc:
            print(exc)
        
    def make_table_cards(self):
        ''' Create cards table if it doesn't exist '''
        if self._type == 'sqlite':    
            sql = f'''
                    select name
                    from sqlite_master
                    where name = 'cards'
                    '''
        else: 
            sql = 'show tables like "cards"'
        try:
            self._cur.execute(sql)
            if self._type == 'mysql':
                exists = self._cur.rowcount != 0
            else:
                exists = len(self._cur.fetchall()) != 0
            if not exists:
                print('Making table cards...')
                time.sleep(0.5)
                self._cur.execute('''
                                CREATE TABLE IF NOT EXISTS cards (
                                cardId varchar(50), 
                                front varchar(20) NOT NULL, 
                                back varchar(20) NOT NULL, 
                                deckId varchar(50), 
                                PRIMARY KEY (cardId), 
                                FOREIGN KEY (deckId) REFERENCES decks (deckId)
                                ON DELETE CASCADE
                                );'''
                            )
            else:
                print('Found cards....')
                time.sleep(0.2)
        except Error as e:
            print(e)
        except Exception as exc:
            print(exc)
        
    def update_user_cache(self, user, new_name=None, action=None):
        ''' 
        Updates the local database cache 
        to reduce calls to the database 
        '''
        index = None
        for i in self.user_cache:
            if i[1] == user.user_name:
                index = self.user_cache.index(i)
        if index is not None:
            if action == 'PUTS':
                self.user_cache[index] = (user.id, new_name)
            elif action == 'DELETE':
                self.user_cache.pop(index)
        
    def update_deck_cache(self, deck, new_name=None, action=None):
        ''' 
        Updates the local database cache 
        to reduce calls to the database 
        '''
        index = None
        for i in self.deck_cache:
            if i[1] == deck.deck_name:
                index = self.deck_cache.index(i)
        if index is not None:
            if action == 'PUTS':
                self.deck_cache[index] = (deck.id, new_name)
            elif action == 'DELETE':
                self.deck_cache.pop(index)
        
    def update_card_cache(self, card, new_front=None, new_back=None, action=None):
        ''' 
        Updates the local database cache 
        to reduce calls to the database 
        '''
        index = None
        for i in self.card_cache:
            if i[0] == card[0]:
                index = self.card_cache.index(i)
        if index is not None:
            if action == 'PUTS':
                self.card_cache[index] = (card[0], new_front, new_back)
            elif action == 'DELETE':
                self.card_cache.pop(index)

    def close(self):
        ''' Close the connection '''
        if self._connection is not None:
            self._connection.close()