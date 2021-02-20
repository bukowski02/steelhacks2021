from flask import Flask, render_template
#import db
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():
#initializes the database
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    create = """
        CREATE TABLE IF NOT EXISTS words (
          id INTEGER PRIMARY KEY,
          word TEXT,
          definition TEXT,
          learned INTEGER,
          learnedDate INTEGER
        );
        """
    c.execute(create)
    insert = """
        INSERT INTO words (id, word, definition) VALUES (0, 'ye', 'alternate form of yes, affirmative, etc')
    """
    c.execute(insert)
    #conn = sqlite3.connect('database.db')
    a = c.execute("SELECT * FROM words")
    return a
    #return render_template("index.html")