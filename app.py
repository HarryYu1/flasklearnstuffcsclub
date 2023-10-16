from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/index")
def show_index():
    return render_template('confirmation.html')