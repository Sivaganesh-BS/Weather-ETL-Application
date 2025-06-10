import sqlite3

from .constants import *

class db_config():
    _connection = None
    _cursor = None


    def __init__(self):
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        self._connection = conn
        self._cursor = cursor


    def execute_query(self,query):
        try:
            response = self._cursor.execute(query)
            self._connection.commit()
            return response
        except Exception as e:
            print(f'Error Occured while executing Query. Error : {e}')
    

    def execute_multiple_query(self,query):
        try:
            for i in query:
                self._cursor.execute(i)
            self._connection.commit()
            
        except Exception as e:
            print(f'Error Occured while executing Query. Error : {e}')

    def close(self):
        try:
            self._connection.close()

        except Exception as ex:
            print(f'Error Occured while closing DB. Error : {ex}')

    def initial_table_creation(self):
        try:
            self.execute_query(LOCATION_TABLE_CREATION)
            self.execute_query(Locations_Data_Query)
            location = ['Coimbatore','Bengaluru','Delhi', 'Chennai']
            for i in location:
                query=TABLE_QUERY.format(location=i)
                self.execute_query(query=query)

        except Exception as e:
            print(f'Error Occured while closing DB. Error : {e}')



if __name__ == '__main__':
    try:
        db_con = db_config()
        # db_con.initial_table_creation() 
        # db_con.execute_query(TABLE_QUERY)
        print('Successfully Executed...')
    
    except Exception as e:
        print(f'Error Occurred. Error: {e}')
