import os
from mysql.connector import connect, Error
from dotenv import load_dotenv

class Database:
    def __init__(self):
        self._cur = None
        self.connect()
    
    def connect(self):
        load_dotenv()
        try:
            self._connection = connect(
            host=os.environ['host'],
            port=os.environ['port'],
            user=os.environ['dbuser'],
            password=os.environ['password'],
            database=os.environ['db']
        )
            self._cur = self._connection.cursor(buffered=True)
        except KeyError as e:
            print(f'KeyError: {e} does not exist')
        except Error as err:
            print(err)
            
    @property
    def connection(self):
        return self._connection
    
    @connection.setter
    def connection(self, connection):
        self._connection = connection
        
    @property
    def cur(self):
        return self._cur
    
    def close(self):
        if self._connection is not None:
            self._connection.close()