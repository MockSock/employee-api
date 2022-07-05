from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


if __name__ == "__main__": 
    app.run(debug=True)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/employees")
def getEmployees():

    return "I will be a get method soon"