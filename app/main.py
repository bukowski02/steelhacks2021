from flask import Flask, render_template
from processing import process

app = Flask(__name__)

@app.route('/')

# don't touch ^^^^

def home():
    return render_template(index.html)

def hello_world():
    return 0
    #f = open("main.html",'r')
    #html = f.read()
    #f.close()

    #html = process(html)
    
    #return html
