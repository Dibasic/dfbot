from config import *
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>200 OK</h1><p>This page exists to return HTTP 200.</p>'

if __name__ == '__main__':
    app.run(host=HOST, port=PORT)