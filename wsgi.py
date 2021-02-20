from app.main import app 
import sqlite3

if __name__ == "__main__": 
        #initializes the database
        conn = sqlite3.connect('database.db')
        create = """
            CREATE TABLE IF NOT EXISTS "words" (
              id INTEGER PRIMARY KEY,
              word TEXT,
              definition TEXT,
              learned INTEGER,
              learnedDate INTEGER,
            );
            """
        conn.execute(create)
        insert = """
            INSERT INTO words (id, word, definition) VALUES (0, 'ye', 'alternate form of yes, affirmative, etc')
        """
        conn.execute(insert)
        app.run()