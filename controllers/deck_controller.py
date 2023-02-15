from models.deck import Deck 
from mysql.connector import Error
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
            print(f'{new_deck.id}, {new_deck.deck_name}, {new_deck.user_id}')
            self.cur.execute(f'INSERT INTO decks (deckId, name, userId) SELECT \'{new_deck.id}\' as deckId, \'{new_deck.deck_name}\' as name, \'{new_deck.user_id}\' as userId FROM decks WHERE (name=\'{new_deck.deck_name}\' and userId=\'{new_deck.user_id}\') HAVING COUNT(*) = 0')
            self.connection.commit()
            print(self.cur.rowcount, "record inserted")
            self.db.deck_cache += [(new_deck.id, new_deck.deck_name)]
            return 5 if self.cur.rowcount == 1 else -5
        except Error as e:
            print(e)
            return -5

    def display_decks(self):
        self._cur_deck = None
        try:
            if len(self.db.deck_cache) == 0:
                print('Connecting to database....')
                sql = f'SELECT deckId, name FROM decks WHERE userId = \'{self._cur_user.id}\' ORDER BY deckId'
                self.cur.execute(sql)
                self.db.deck_cache += [i for i in self.cur if i not in self.db.deck_cache]
                time.sleep(1)
        except Error as e:
            print(e)
        return 6

    def update_deck_name(self, name=None):
        name = self._cur_deck.deck_name if name is None else name
        try:
            self.cur.execute(f'SELECT name FROM decks WHERE name = \'{name}\'')
            deck = self.cur.fetchone()
            if deck is not None:
                new_name = input('Enter a new name: ')
                self.cur.execute(f'UPDATE decks SET name = \'{new_name}\' WHERE name = \'{name}\'')
                self.db.update_deck_cache(self._cur_deck, new_name)
                if self._cur_deck:
                    self._cur_deck.deck_name = new_name
                self.connection.commit()
                print(self.cur.rowcount, 'record updated')
                return 8
            else: 
                return -9
        except Error as e:
            print(e)
            return -9
    
    def delete_deck(self, deckId):
        # TODO: Delete deck from cache
        try:
            self.cur.execute(f'SELECT deckId, name, userId FROM decks WHERE deckId = \'{deckId}\'')
            deck = self.cur.fetchone()
            if deck is not None:
                if (deck[2]) != self._cur_user.id:
                    return -9
                else:
                    self.cur.execute(f'DELETE FROM decks WHERE deckId = \'{deckId}\' AND userId = \'{self._cur_user.id}\'')
                    print(self.cur.rowcount, 'record deleted')
                    self.connection.commit()
                    return -8
            else:
                return -9
        except Error as e:
            print(e)
        
    def view_deck(self, name):
        # TODO: Change to use cache
        try:
            self.cur.execute(f'SELECT * FROM decks WHERE name = BINARY \'{name}\'')
            row = self.cur.fetchone()
            if row is not None:
                self._cur_deck = Deck(deck_id=row[0], deck_name=row[1], user_id=row[2])
                return 10
            else:
                row = None
                return -9
        except Error as e:
            print(e)

# insert into decks (deckId, name, userId)
# select {deckId} as deckId, {name} as name, {userId} as userId
# where (name={name}, userId={userId})
# having count(*) = 0;