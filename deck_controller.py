from deck import Deck 
from mysql.connector import Error


class DeckController:
    
    def __init__(self, db):
        self._cur_user = None
        self.cur = db.cursor()
        self.db = db
        
    @property
    def cur_user(self):
        return self._cur_user
    
    @cur_user.setter
    def cur_user(self, cur_user):
        self._cur_user = cur_user
    
    def create_deck(self):
        deck_name = input('Deck name: ')
        new_deck = Deck(deck_name, self._cur_user.id)
        try:
            print(f'{new_deck.id}, {new_deck.deck_name}, {new_deck.user_id}')
            self.cur.execute(f'INSERT INTO decks (deckId, name, userId) VALUES (\'{new_deck.id}\', \'{new_deck.deck_name}\', \'{new_deck.user_id}\')')
            self.db.commit()
            print(self.cur.rowcount, "record inserted")
            return 5
        except Error as e:
            print(e)
            return -5

    def display_decks(self):
        # [print(f'{self._cur_user.decks[i].deck_name}, {self._cur_user.decks[i].id}') for i in self._cur_user.decks]
        self.cur.execute(f'SELECT deckId, name FROM decks WHERE userId = \'{self._cur_user.id}\' ORDER BY deckId')
        for (deckId, name) in self.cur:
            print(f'{deckId}, {name}')

    def update_deck_name(self, name):
        try:
            self.cur.execute(f'SELECT name FROM decks WHERE name = \'{name}\'')
            deck = self.cur.fetchone()
            if deck is not None:
                new_name = input('Enter a new name: ')
                self.cur.execute(f'UPDATE decks SET name = \'{new_name}\' WHERE name = \'{name}\'')
                self.db.commit()
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