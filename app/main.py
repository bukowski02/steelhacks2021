from sqlite3 import *
from flask import Flask, render_template, g, request
from processing import *

app = Flask(__name__)

DB_PATH = 'database.db'
DB_NAME = ''
DB_COLS = ('col1', 'col2', 'col3')
CARD_NAME = ''
CARD_COLS = ('col1', 'col2', 'col3')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/addreq', methods=['POST', 'GET'])
def addreq():
    if request.method == 'POST':
        output = ''
        try:
            word = request.form['word']
            add_to_flash_cards(word)
            output = 'Word successfully added.'
        except:
            output = 'Error: word could not be added.'
        finally:
            return render_template('success.html', output=output)


def open_db() -> Cursor:
    db = getattr(g, '_database', None)
    if db is not None:
        db = g._database = connect(DB_PATH)
    return db.cursor()


@app.teardown_appcontext
def close_db() -> None:
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def get_db() -> list:
    cur = open_db()
    get_db_sql = f'SELECT * FROM {DB_NAME}'
    cur.execute(get_db_sql)
    return cur.fetchall()


def add_to_db(params: tuple) -> None:
    cur = open_db()
    add_to_db_sql = f'INSERT INTO {DB_NAME} ' \
                    f'({DB_COLS[0]}, {DB_COLS[1]}, {DB_COLS[2]}) ' \
                    f'VALUES ({params[0]}, {params[1]}, {params[2]})'
    cur.execute(add_to_db_sql)
    cur.close()


def add_to_flash_cards(word: str):
    cur = open_db()
    add_to_cards_sql = f'INSERT INTO {CARD_NAME}'  # Incomplete
    cur.execute(add_to_cards_sql)
    cur.close()
