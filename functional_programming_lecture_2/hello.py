from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world(name):
    return f'Hello, {name}!'
