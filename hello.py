from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/hello/Thomas')
def information():
    return render_template('hello.html')
    

@app.route("/index")
def index():
    return "test"


@app.route("/soccer")
def soccer():
    return "I love soccer"

