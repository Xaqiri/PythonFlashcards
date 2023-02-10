class User:
    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password
        
    def setUserName(self, new_name):
        self.user_name = new_name
    
    def setPassword(self, new_password):
        self.password = new_password
    
    def getUserName(self):
        return self.user_name
    
    def getPassword(self):
        return self.password
    
    