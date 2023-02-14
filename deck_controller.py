from deck import Deck 
from mysql.connector import Error


class DeckController:
    
    def __init__(self, db):
        self._cur_user = None
        self._cur_deck = None
        self.db = db.connection
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
            self.db.commit()
            print(self.cur.rowcount, "record inserted")
            return 5 if self.cur.rowcount == 1 else -5
                
        except Error as e:
            print(e)
            return -5

    def display_decks(self):
        self._cur_deck = None
        try:
            self.cur.execute(f'SELECT deckId, name FROM decks WHERE userId = \'{self._cur_user.id}\' ORDER BY deckId')
            for (deckId, name) in self.cur:
                print(f'{deckId}, {name}')
        except Error as e:
            print(e)

    def update_deck_name(self, name=None):
        name = self._cur_deck.deck_name is name is None
        try:
            self.cur.execute(f'SELECT name FROM decks WHERE name = \'{name}\'')
            deck = self.cur.fetchone()
            if deck is not None:
                new_name = input('Enter a new name: ')
                self.cur.execute(f'UPDATE decks SET name = \'{new_name}\' WHERE name = \'{name}\'')
                if self._cur_deck:
                    self._cur_deck.deck_name = new_name
                self.db.commit()
                print(self.cur.rowcount, 'record updated')
                return 8
            else: 
                return -9
        except Error as e:
            print(e)
    
    def delete_deck(self, deckId):
        self.cur.execute(f'SELECT deckId, name, userId FROM decks WHERE deckId = \'{deckId}\'')
        deck = self.cur.fetchone()
        if deck is not None:
            if (deck[2]) != self._cur_user.id:
                return -9
            else:
                self.cur.execute(f'DELETE FROM decks WHERE deckId = \'{deckId}\' AND userId = \'{self._cur_user.id}\'')
                print(self.cur.rowcount, 'record deleted')
                self.db.commit()
                return -8
        else:
            return -9
        
    def view_deck(self, name):
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