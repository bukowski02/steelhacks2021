from flask import Flask
from processing import process

app = Flask(__name__)

@app.route('/')

# don't touch 


def hello_world():

    f = open("main.html",'r')
    html = f.read()
    f.close()

    html = process(html)
    
    return html
