from tokenize import String
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class EmployeeList(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    

if __name__ == "__main__": 
    app.run(debug=True)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/employees")
def getEmployees():

    return "I will be a get method soon"