import sqlite3

#initializes the database
def dbInit():
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
    
