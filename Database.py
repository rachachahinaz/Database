import mysql.connector

class Database:
    def __init__(self, db_name="newdatabase"):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="racharacha123",
            database=db_name
        )
        self.create_tables()

    def create_tables(self):
        with self.conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(100) NOT NULL,
                    gmail VARCHAR(100) UNIQUE NOT NULL,
                    password_name VARCHAR(100) NOT NULL,
                    password_gmail VARCHAR(100) NOT NULL
                )
            """)
            self.conn.commit()

    def add_user(self, name, gmail, password_name, password_gmail):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO users (name, gmail, password_name, password_gmail) 
                    VALUES (%s, %s, %s, %s)
                """, (name, gmail, password_name, password_gmail))
                self.conn.commit()
                print(f"User {name} registered successfully!")
        except mysql.connector.IntegrityError:
            print("Gmail already exists!")
        except Exception as e:
            print(f"An error occurred: {e}")

    def get_user(self, identifier, password, use_gmail=False):
        cursor = self.conn.cursor()
        if use_gmail:
            cursor.execute("SELECT * FROM users WHERE gmail = %s AND password_gmail = %s", (identifier, password))
        else:
            cursor.execute("SELECT * FROM users WHERE name = %s AND password_name = %s", (identifier, password))
        return cursor.fetchone()
