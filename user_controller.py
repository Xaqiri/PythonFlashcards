from user import User 
from database import db

class UserController:
    
    def __init__(self):
        self.cur_user = None
    
    def getCurUser(self):
        return self.cur_user
    
    def get_user_info(self):
        name = input('Username: ')
        password = input('Password: ')
        user = User(name, password)
        return user
        
    def create_new_user(self):
        new_user = self.get_user_info()
        if new_user.getUserName() in db.keys():
            return -4
        else: 
            db[new_user.getUserName()] = new_user
            return 1

    def sign_in(self):
        check_user = self.get_user_info()
        if check_user.getUserName() not in db.keys():
            return -2
        else:
            user = db[check_user.getUserName()]
            if user.getPassword() != check_user.getPassword():
                return -3
            else:
                self.cur_user = user
                return 2

    def signOut(self):
        self.cur_user = None
    
    def display_users(self):
        [print(f'{db[i].getUserName()}, {db[i].getId()}') for i in db]
