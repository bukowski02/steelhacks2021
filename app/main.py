from flask import Flask, render_template
#import db
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():
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
    #conn = sqlite3.connect('database.db')
    print(conn.execute("SELECT * FROM words"))
    return
    #return render_template("index.html")