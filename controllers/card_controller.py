from models.card import Card
from mysql.connector import Error
import time 

class CardController:
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
    
    def create_card(self, front, back, deck_id):
        new_card = Card(front, back, deck_id)
        print(f'{new_card.id}, {new_card.front}, {new_card.back}, {new_card.deck_id}')
        try:
            sql = 'INSERT INTO cards (cardId, front, back, deckId) VALUES (%s, %s, %s, %s)'
            val = (new_card.id, front, back, deck_id)
            self.cur.execute(sql, val)
            self.connection.commit()
            self.db.card_cache += [(new_card.id, new_card.front, new_card.back)]
        except Error as e:
            print(e)
        print(self.cur.rowcount, "record inserted")
        return 11
    
    def display_cards(self):
        try:
            if len(self.db.card_cache) == 0:
                print('Connecting to database....')
                sql = f'SELECT cardId, front, back FROM cards WHERE deckId = \'{self._cur_deck.id}\' ORDER BY front'
                self.cur.execute(sql)
                self.db.card_cache += [i for i in self.cur if i not in self.db.card_cache]
                time.sleep(1)
        except Error as e:
            print(e)
        return 12