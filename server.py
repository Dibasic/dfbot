from config import *
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    json_data = {'Hello': 'World!'}
    return jsonify(json_data)


if __name__ == '__main__':
app.run()