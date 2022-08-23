from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello():
    return '<h1>Hello, World! </h1> <h2> I am doing Good </h2>'
