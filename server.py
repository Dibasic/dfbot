import config
from flask import Flask

app = Flask(__name__)
app.run(HOST, PORT)