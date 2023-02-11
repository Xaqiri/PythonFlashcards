import uuid

class Deck:
    def __init__(self, deck_name, user_id):
        self.id = uuid.uuid4()
        self.deck_name = deck_name
        self.user_id = user_id
        self.cards = {}
        
    def setDeckName(self, new_name):
        self.deck_name = new_name
        
    def getId(self):
        return self.id
    
    def getDeckName(self):
        return self.deck_name
    
    def getUser(self):
        return self.user_id