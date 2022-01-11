import sys
from flask import Flask

args = sys.argv
HTMLData = args[1]

app = Flask(__name__)

@app.route("/")
def run():
    return HTMLData