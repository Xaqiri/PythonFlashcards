from user import User 
from mysql.connector import Error

class UserController:
    
    def __init__(self, db):
        self._cur_user = None
        self.db = db
        self.cur = db.cursor()
    
    @property
    def cur_user(self):
        return self._cur_user
    
    @cur_user.setter
    def cur_user(self, cur_user):
        self._cur_user = cur_user
    
    def get_user_info(self):
        name = input('Username: ')
        password = input('Password: ')
        user = User(name, password)
        return user
        
    def create_new_user(self):
        new_user = self.get_user_info()
        sql = "INSERT INTO users (userId, name, password) VALUES (%s, %s, %s)"
        val = (new_user.id, new_user.user_name, new_user.password)
        try:
            self.cur.execute(sql, val)
            self.db.commit()
            print(self.cur.rowcount, "record inserted")
            return 1
        except Error as e:
            return -4
        
    def display_users(self):
        sql = "SELECT userId, name FROM users ORDER BY userId"
        self.cur.execute(sql)
        for (userId, name) in self.cur:
            print(f'{userId} {name}')
            
    def update_user_name(self):
        try:
            new_name = input('Enter new username: ')
            if len(new_name) == 0:
                return -2
            else:
                self._cur_user.user_name = new_name
                self.cur.execute(f'UPDATE users SET users.name = \'{new_name}\' WHERE users.userId = \'{self._cur_user.id}\'')
                self.db.commit()
                self._cur_user.user_name = new_name
                return 9
        except Error as e:
            print(e)
            
    def delete_user(self):
        self.cur.execute(f'DELETE FROM users WHERE userId = \'{self._cur_user.id}\'')
        self._cur_user = None
        self.db.commit()
        return -7
    
    def sign_in(self):
        check_user = self.get_user_info()
        try:
            self.cur.execute(f'SELECT userId, name, password FROM users WHERE name = BINARY \'{check_user.user_name}\'')
            row = self.cur.fetchone()
        except Error as e:
            print(e)
            return -2
        
        if row is None:
            return -6
        else:
            if check_user.password != row[2]:
                return -3
            else:
                self._cur_user = User(id=row[0], user_name=row[1], password=row[2])
                return 2

    def sign_out(self):
        self._cur_user = None
    
    
