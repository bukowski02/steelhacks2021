from flask import Flask, render_template, request, url_for
from . import db #this is the syntax for how to import files in same directory you must use
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():
    db.init()

    return render_template("index.html")

@app.route('/post',methods = ['POST'])
def postProcessing():
    name = request.form['nm']
    return redirect(url_for('success',name = name))

@app.route('/success')
def nameHello(name):
    return "hello"+name