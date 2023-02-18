from models.card import Card
from mysql.connector import Error
from sqlite3 import Error
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
    
    def create_card(self):
        front = input('Front: ')
        back = input('Back: ')
        new_card = Card(front, back, self._cur_deck.id)
        try:
            sql = f'INSERT INTO cards (cardId, front, back, deckId) VALUES (\'{new_card.id}\', \'{new_card.front}\', \'{new_card.back}\', \'{new_card.deck_id}\')'
            self.cur.execute(sql)
            self.connection.commit()
            self.db.card_cache += [(new_card.id, new_card.front, new_card.back)]
        except Error as e:
            print(e)
        print(self.cur.rowcount, "record inserted")
        return 'card_created'
    
    def display_cards(self):
        try:
            if len(self.db.card_cache) == 0:
                print('Connecting to database....')
                sql = f'SELECT cardId, front, back FROM cards WHERE deckId = \'{self._cur_deck.id}\' ORDER BY front'
                self.cur.execute(sql)
                self.db.card_cache += [i for i in self.cur if i not in self.db.card_cache]
                time.sleep(0.5)
        except Error as e:
            print(e)
        [print(i) for i in self.db.card_cache]
    
    def update_card(self):
        card_id = input('Enter id of card to edit: ')
        front = input('Enter front of card: ')
        back = input('Enter back of card: ')
        
        try:
            sql = f'SELECT cardId, front, back FROM cards WHERE cardId = \'{card_id}\''
            self.cur.execute(sql)
            old_card = self.cur.fetchone()
            if old_card is not None:
                front = old_card.front if front is None else front
                back = old_card.back if back is None else back
                sql = f'''
                        UPDATE cards 
                        SET front = \'{front}\', back = \'{back}\'
                        WHERE  cardId = \'{old_card[0]}\'
                        '''
                self.cur.execute(sql)
                self.connection.commit()
                print(self.cur.rowcount, 'record updated')
                self.db.update_card_cache(old_card, new_front=front, new_back=back, action='PUTS')
                return 'card_updated'
            else:
                return 'card_not_deleted'
        except Error as e:
            print(e)
            
    def delete_card(self, card_id):
        try:
            sql = f'SELECT * FROM cards WHERE cardId = \'{card_id}\''
            self.cur.execute(sql)
            card = self.cur.fetchone()
            if card is not None:
                sql = f'DELETE FROM cards WHERE cardId = \'{card_id}\''
                self.cur.execute(sql)
                self.connection.commit()
                print(self.cur.rowcount, 'record deleted')
                self.db.update_card_cache(card, action='DELETE')
                return 'card_deleted'
            return 'card_not_deleted'
        except Error as e:
            print(e)
    
    def delete_all_cards(self, deck_id):
        self.cur.execute(f'''
                        SELECT cardId 
                        FROM cards 
                        WHERE deckId = \'{deck_id}\'
                        ''')
        cards = self.cur.fetchall()
        for i in cards:
            self.delete_card(i[0])
        print('Cards deleted')
