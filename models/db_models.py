from settings.settings_db import db
from flask_login import UserMixin

""" models for user database """

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(50), unique=True) #email must be unique
    password = db.Column(db.String(150))
    bills = db.relationship("Rent", "Market") #set relationship databases

""" models for bills database """

class Rent(db.Model):
    __tablename__ = "rent"
    id = db.Column(db.Integer, primary_key=True)
    rent = db.Column(db.Integer)
    expenses = db.Column(db.Integer)
    electricity = db.Column(db.Integer)
    gas = db.Column(db.Integer)
    water = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True)) #takes current time when object is created
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

""" models for market database """

class Market(db.Model):
    __tablename__ = "market"
    id = db.Column(db.Integer, primary_key=True)
    market = db.Column(db.Integer)
    market_list = db.Column(db.String(1000)) # <- should be a dictionary with keys and values
    delivery = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
