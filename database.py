import os
from mysql.connector import connect, Error
from dotenv import load_dotenv
import time
class Database:
    def __init__(self):
        self._cur = None
        self.connect()
        self.user_cache = []
        self.deck_cache = []
        self.card_cache = []
        
    def connect(self):
        load_dotenv()
        try:
            print('Connecting....')
            self._connection = connect(
            host=os.environ['host'],
            port=os.environ['port'],
            user=os.environ['dbuser'],
            password=os.environ['password'],
            database=os.environ['db']
        )
            self._cur = self._connection.cursor(buffered=True)
        except KeyError as e:
            print(f'KeyError: {e} does not exist')
        except Error as err:
            print(err)
        
        if self._cur is None:
            print('Do you want to create a local database? ')
            
        try:
            self._cur.execute('show tables like "users"')
            if self._cur.rowcount == 0:
                self.make_table_users()
            self._cur.execute('show tables like "decks"')
            if self._cur.rowcount == 0:
                self.make_table_decks()
            self._cur.execute('show tables like "cards"')
            if self._cur.rowcount == 0:
                self.make_table_cards()
        except Error as e:
            print(e)
            
    @property
    def connection(self):
        return self._connection
    
    @connection.setter
    def connection(self, connection):
        self._connection = connection
        
    @property
    def cur(self):
        return self._cur
    
    def make_table_users(self):
        print('Making table users...')
        self._cur.execute('''
            CREATE TABLE IF NOT EXISTS users (
            userId varchar(50), 
            name varchar(50) NOT NULL UNIQUE,
            password varchar(20) NOT NULL, 
            PRIMARY KEY (userId)
            );'''
        )
    
    def make_table_decks(self):
        print('Making table decks...')
        self._cur.execute('''
            CREATE TABLE IF NOT EXISTS decks (
            deckId varchar(50), 
            name varchar(20) NOT NULL,
            userId varchar(50), 
            PRIMARY KEY (deckId), 
            FOREIGN KEY (userId) REFERENCES users (userId)
            );'''
        )
    
    def make_table_cards(self):
        print('Making table cards...')
        self._cur.execute('''
            CREATE TABLE IF NOT EXISTS cards (
            cardId varchar(50), 
            front varchar(20) NOT NULL, 
            back varchar(20) NOT NULL, 
            deckId varchar(50), 
            PRIMARY KEY (cardId), 
            FOREIGN KEY (deckId) REFERENCES decks (deckId)
            );'''
        )
        
    def update_user_cache(self, user, new_name=None, action=None):
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
        if self._connection is not None:
            self._connection.close()