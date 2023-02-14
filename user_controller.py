from user import User 
from mysql.connector import Error

class UserController:
    
    def __init__(self, db):
        self.cur_user = None
        self.db = db
        self.cur = db.cursor()
    
    def getCurUser(self):
        return self.cur_user
    
    def get_user_info(self):
        name = input('Username: ')
        password = input('Password: ')
        user = User(name, password)
        return user
        
    def create_new_user(self):
        new_user = self.get_user_info()
        sql = "INSERT INTO users (userId, name, password) VALUES (%s, %s, %s)"
        val = (new_user.getId(), new_user.getUserName(), new_user.getPassword())
        try:
            self.cur.execute(sql, val)
            self.db.commit()
            print(self.cur.rowcount, "record inserted")
            return 1
        except Error as e:
            return -4
        
    def update_user_name(self):
        try:
            new_name = input('Enter new username: ')
            self.cur.execute(f'UPDATE users SET users.name = \'{new_name}\' WHERE users.userId = \'{self.cur_user.getId()}\'')
            self.db.commit()
            self.cur_user.setUserName(new_name)
        except Error as e:
            print(e)
            
    def sign_in(self):
        check_user = self.get_user_info()
        try:
            self.cur.execute(f'SELECT userId, name, password FROM users WHERE name = BINARY \'{check_user.getUserName()}\'')
            row = self.cur.fetchone()
        except Error as e:
            print(e)
            return -2
        
        if row is None:
            return -6
        else:
            if check_user.getPassword() != row[2]:
                return -3
            else:
                self.cur_user = User(userId=row[0], user_name=row[1], password=row[2])
                return 2

    def signOut(self):
        self.cur_user = None
    
    def display_users(self):
        sql = "SELECT userId, name FROM users ORDER BY userId"
        self.cur.execute(sql)
        for (userId, name) in self.cur:
            print(f'{userId} {name}')
