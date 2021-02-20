from flask import Flask, render_template
import db

app = Flask(__name__)


@app.route('/')
def home():
    conn = sqlite3.connect('database.db')
    print(conn.execute("SELECT * FROM words")
    return
    #return render_template("index.html")