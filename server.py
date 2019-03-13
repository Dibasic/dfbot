from config import *
from flask import Flask

app = Flask(__name__)
app.run(HOST, PORT)