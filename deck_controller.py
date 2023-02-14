from deck import Deck 
from mysql.connector import Error


class DeckController:
    
    def __init__(self, cur_user, db):
        self.cur_user = cur_user
        self.cur = db.cursor()
        self.db = db
        
    def setCurUser(self, cur_user):
        self.cur_user = cur_user
        
    def create_deck(self):
        deck_name = input('Deck name: ')
        new_deck = Deck(deck_name, self.cur_user.getId())
        try:
            print(f'{new_deck.getId()}, {new_deck.getDeckName()}, {new_deck.getUserId()}')
            self.cur.execute(f'INSERT INTO decks (deckId, name, userId) VALUES (\'{new_deck.getId()}\', \'{new_deck.getDeckName()}\', \'{new_deck.getUserId()}\')')
            self.db.commit()
            print(self.cur.rowcount, "record inserted")
            return 5
        except Error as e:
            print(e)
            return -5

    def display_decks(self):
        # [print(f'{self.cur_user.decks[i].getDeckName()}, {self.cur_user.decks[i].getId()}') for i in self.cur_user.decks]
        self.cur.execute(f'SELECT deckId, name FROM decks WHERE userId = \'{self.cur_user.getId()}\' ORDER BY deckId')
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
            if (deck[2]) != self.cur_user.getId():
                return -9
            else:
                self.cur.execute(f'DELETE FROM decks WHERE deckId = \'{deckId}\' AND userId = \'{self.cur_user.getId()}\'')
                print(self.cur.rowcount, 'record deleted')
                self.db.commit()
                return -8
        else:
            return -9