import uuid

class Deck:
    def __init__(self, deck_name, user_id, deck_id=None):
        self._id = str(uuid.uuid4()) if deck_id is None else deck_id
        self._deck_name = deck_name
        self._user_id = user_id

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def deck_name(self):
        return self._deck_name
    
    @deck_name.setter
    def deck_name(self, deck_name):
        self._deck_name = deck_name
        
    @property
    def user_id(self):
        return self._user_id
    
    @user_id.setter
    def user_id(self, user_id):
        self._password = user_id