from models.deck import Deck 
from mysql.connector import Error
from sqlite3 import Error
import time

class DeckController:
    
    def __init__(self, db):
        self._cur_user = None
        self._cur_deck = None
        self.db = db
        self.connection = db.connection
        self.cur = db.cur
        
    @property
    def cur_user(self):
        return self._cur_user
    
    @cur_user.setter
    def cur_user(self, cur_user):
        self._cur_user = cur_user
    
    @property
    def cur_deck(self):
        return self._cur_deck
    
    @cur_deck.setter
    def cur_deck(self, cur_deck):
        self._cur_deck = cur_deck
    
    def create_deck(self):
        deck_name = input('Deck name: ')
        new_deck = Deck(deck_name, self._cur_user.id)
        try:
            self.cur.execute(f'''
            select * from decks
            where
            name = (select name from decks where name = \'{new_deck.deck_name}\') and
            userId = (select userId from users where userId = \'{new_deck.user_id}\')
            ''')
            row = len(self.cur.fetchall()) if self.db.type == 'sqlite' else self.cur.rowcount
            if row == 0:
                self.cur.execute(
                    f'''
                    INSERT INTO decks (deckId, name, userId)
                    VALUES (\'{new_deck.id}\', \'{new_deck.deck_name}\', \'{new_deck.user_id}\')             
                    ''')
                self.connection.commit()
                print(self.cur.rowcount, "record inserted")
                self.db.deck_cache += [(new_deck.id, new_deck.deck_name)]
                return 'deck_created'
            else:
                return 'deck_found'
        except Error as e:
            print(e)
            time.sleep(0.5)
            return 'deck_found'
        except Exception as exc:
            print(exc)

    def display_decks(self):
        self._cur_deck = None
        try:
            if len(self.db.deck_cache) == 0:
                print('Connecting to database....')
                sql = f'SELECT deckId, name, userId FROM decks WHERE userId = \'{self._cur_user.id}\' ORDER BY deckId'
                self.cur.execute(sql)
                self.db.deck_cache += [i for i in self.cur if i not in self.db.deck_cache]
                time.sleep(0.5)
        except Error as e:
            print(e)
        [print(i) for i in self.db.deck_cache]

    def update_deck_name(self, name=None):
        name = self._cur_deck.deck_name if name is None else name
        try:
            self.cur.execute(f'SELECT name FROM decks WHERE name = \'{name}\'')
            deck = self.cur.fetchone()
            if deck is not None:
                new_name = input('Enter a new name: ')
                self.cur.execute(f'UPDATE decks SET name = \'{new_name}\' WHERE name = \'{name}\'')
                self.db.update_deck_cache(self._cur_deck, new_name, action='PUTS')
                if self._cur_deck:
                    self._cur_deck.deck_name = new_name
                self.connection.commit()
                print(self.cur.rowcount, 'record updated')
                return 'deck_updated'
            else: 
                return 'deck_found'
        except Error as e:
            print(e)
            return 'deck_not_found'
    
    def delete_deck(self):
        deckId = self._cur_deck.id if self._cur_deck else input('Deck id: ') 
        try:
            self.cur.execute(f'SELECT deckId, name, userId FROM decks WHERE deckId = \'{deckId}\'')
            deck = self.cur.fetchone()
            if deck is not None:
                if (deck[2]) != self._cur_user.id:
                    return 'deck_not_found'
                else:
                    self.cur.execute(f'DELETE FROM decks WHERE deckId = \'{deckId}\' AND userId = \'{self._cur_user.id}\'')
                    self.connection.commit()
                    self.db.update_deck_cache(Deck(deck_id=deck[0], deck_name=deck[1], user_id=deck[2]), action='DELETE')
                    self._cur_deck = None
                    print(f'deck {deckId} deleted')
                    return 'deck_deleted'
            else:
                return 'deck_not_found'
        except Exception as exc:
            print(exc)
        except Error as e:
            print(e)
        
    def delete_all_deck(self, user_id, card_controller):
        try:
            self.cur.execute(f'SELECT deckId FROM decks WHERE userId = \'{user_id}\'')
            decks = self.cur.fetchall()
            for i in decks:
                card_controller.delete_all_card(i[0])
                self._cur_deck = Deck(deck_id=i[0], deck_name=None, user_id=None)
                self.delete_deck()
                time.sleep(0.2)
        except Error as e:
            print(e)
    
    def view_deck(self, card):
        name = input('Deck name: ')
        try:
            self.cur.execute(f'SELECT * FROM decks WHERE name = \'{name}\'')
            row = self.cur.fetchone()
            if row is not None:
                self._cur_deck = Deck(deck_id=row[0], deck_name=row[1], user_id=row[2])
                card.cur_deck = self._cur_deck
                return 'use_deck'
            else:
                row = None
                return 'deck_not_found'
        except Error as e:
            print(e)

    def exit_deck(self):
        self._cur_deck = None
        self.db.card_cache = []
        
# Copied from stackoverflow. Saving because I don't understand it
# Replaced with 2 queries I wrote, first to check if an item exists
# and second to insert the item into the table if the previous conditions are false
# self.cur.execute(f'
#   INSERT INTO decks (deckId, name, userId) 
#   SELECT \'{new_deck.id}\' as deckId, \'{new_deck.deck_name}\' as name, \'{new_deck.user_id}\' as userId 
#   FROM decks 
#   WHERE (name=\'{new_deck.deck_name}\' and userId=\'{new_deck.user_id}\') 
#   HAVING COUNT(*) = 0')
