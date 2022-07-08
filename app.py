from flask import Flask, jsonify, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# Config work
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employee.db'

#  Database Work
db = SQLAlchemy(app)
ma = Marshmallow(app)

class Employee(db.Model):
    employee_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    role = db.Column(db.String(50))
    employment_type = db.Column(db.String(50))

class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('employee_id', 'full_name', 'role', 'employment_type')

employee_schema = EmployeeSchema(many=True)

if __name__ == "__main__":
    db.create_all() 
    # to make the app run on local host, use command 
    # flask run -h localhost -p 5000
    app.run()

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/employees")
def getEmployees():
    entries = Employee.query.all()
    result = employee_schema.dump(entries)
    return jsonify(result)