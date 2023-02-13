from deck import Deck 

class DeckController:
    
    def __init__(self, cur_user):
        self.cur_user = cur_user
        
    def setCurUser(self, cur_user):
        self.cur_user = cur_user
        
    def create_deck(self):
        deck_name = input('Deck name: ')
        if deck_name in self.cur_user.decks:
            return -5
        else:
            new_deck = Deck(deck_name, self.cur_user.getId())
            self.cur_user.decks[deck_name] = new_deck
            return 5

    def display_decks(self):
        [print(f'{self.cur_user.decks[i].getDeckName()}, {self.cur_user.decks[i].getId()}') for i in self.cur_user.decks]
