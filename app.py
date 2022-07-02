from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask("__name__")

if "__name__" == "__main__": 
    app.run(debug=True)

@app.route("/")
def hello_world():
    return "Hello World"