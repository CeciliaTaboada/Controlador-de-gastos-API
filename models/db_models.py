from flask_sqlalchemy import SQLAlchemy, func
from settings.settings_db import app_db

db = SQLAlchemy(app_db) #init database

""" models for user database """

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(50), unique=True) #email must be unique
    password = db.Column(db.String(150))
    bills = db.relationship("Rent", "Market")

""" models for bills database """

class Rent(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer)
    expenses = db.Column(db.Integer)
    electricity = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    water = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default = func.now()) #takes current time when object is created
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class Market(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    market = db.Column(db.Integer)
    delivery = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default = func.now())
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))