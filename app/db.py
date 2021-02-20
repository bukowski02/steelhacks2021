def hello():
    return "helloaawea"

def init():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    create = """
        CREATE TABLE IF NOT EXISTS words (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          word TEXT,
          possibleDefs TEXT
        );
        CREATE TABLE IF NOT EXISTS flashcards (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          word TEXT,
          definition TEXT,
          exampleLClipID INTEGER,
          examplePhrase TEXT,
          learned INTEGER
        );
        CREATE TABLE IF NOT EXISTS flashcardsets (
          id INTEGER
          flashcards TEXT
        ):
        """
    c.execute(create)

"""
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

this is how you insert:
    insert = "INSERT INTO words (id, word, definition) VALUES (0, 'ye', 'alternate form of yes, affirmative, etc')"
    c.execute(insert)

this is how you select:
    c.execute("SELECT * FROM words")
    a = c.fetchall()
a contains the results as a matrix
"""