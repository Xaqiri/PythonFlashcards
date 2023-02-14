import uuid

class Card:
    
    def __init__(self, front, back, deck_id, id=None):
        self._id = str(uuid.uuid4()) if id is None else id
        self._front = front
        self._back = back
        self._deck_id = deck_id

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def front(self):
        return self._front
    
    @front.setter
    def front(self, front):
        self._front = front
        
    @property
    def back(self):
        return self._back
    
    @back.setter
    def back(self, back):
        self._back = back
        
    @property
    def deck_id(self):
        return self._deck_id
    
    @deck_id.setter
    def deck_id(self, deck_id):
        self._deck_id = deck_id