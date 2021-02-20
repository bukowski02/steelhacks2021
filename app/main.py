from flask import Flask, render_template
from processing import process

app = Flask(__name__)



@app.route('/')
def home():
    return render_template("index.html")