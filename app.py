from flask import Flask
from random import random 


app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/number")
def number():
    return random()

if __name__ =='__main__':
    app.run(debug=True)
 