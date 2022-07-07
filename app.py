from flask import Flask, jsonify, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# Config work
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'

#  Database Work
db = SQLAlchemy(app)

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)


if __name__ == "__main__": 
    app.run(debug=True)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/employees")
def getEmployees():

    return "I will be a get method soon"