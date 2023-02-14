import uuid
class User:
    def __init__(self, user_name, password, id=None):
        self._id = str(uuid.uuid4()) if id is None else id
        self._user_name = user_name
        self._password = password

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
    
    @property
    def user_name(self):
        return self._user_name
    
    @user_name.setter
    def user_name(self, user_name):
        self._user_name = user_name
        
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
        