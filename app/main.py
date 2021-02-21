from flask import Flask, render_template, request, url_for, redirect
from . import db #this is the syntax for how to import files in same directory you must use
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():
    db.init()

    return render_template("index.html")

@app.route('/post',methods = ['POST'])
def postProcessing():
    """
    if request.form['1']:
        blah = request.form['1']
    elif request.form['2']:
        ..."""
    user = request.form['nm']
    return redirect(url_for('success',name = user))

@app.route('/success/<name>')
def success(name):
    return "hello %s" % name