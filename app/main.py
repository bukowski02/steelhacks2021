from flask import Flask
app = Flask(__name__)

@app.route('/')

# don't touch ^^^^^^



def hello_world():
    return 'Hello, World!'