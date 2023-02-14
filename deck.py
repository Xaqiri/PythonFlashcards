import uuid

class Deck:
    def __init__(self, deck_name, user_id, deckId=None):
        self.id = str(uuid.uuid4()) if deckId is None else deckId
        self.deck_name = deck_name
        self.user_id = user_id
        
    def setDeckName(self, new_name):
        self.deck_name = new_name
        
    def getId(self):
        return self.id
    
    def getDeckName(self):
        return self.deck_name
    
    def getUserId(self):
        return self.user_id
    
    