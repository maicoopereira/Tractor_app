import sqlite3
import json

def main():
    print("Database connection file.")

class DatabaseCursor:
    database = ""
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    
    def __init__(self, database):
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        

    #estudar como usar o execute com parametros e construir essa funcao.
    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.conn.commit()
        return self.cursor.fetchall()
        
        
    
    def close(self):
        self.conn.close()
        self.cursor.close()

    def get_connection(self):
        return self.conn
    def get_cursor(self):
        return self.cursor
    def get_database(self):
        return self.database
    
    def set_database(self, database):
        self.database = database
        self.conn = sqlite3.connect(self.database)
        self.cursor = self.conn.cursor()
        if database != "":
            print(f"Connected to database: {self.database}")
            print(f"connection object: {self.conn}")
            print(f"cursor object: {self.cursor}")
            print('''
            You can now use the database connection and cursor.''')
        








if __name__ == "__main__":
    main()