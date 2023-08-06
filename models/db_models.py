from settings.settings_db import db
from flask_login import UserMixin

""" models for user database """

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(50), unique=True) #email must be unique
    password = db.Column(db.String(255))
    rent = db.relationship("Rent", uselist=False, back_populates="users", cascade="all, delete-orphan", single_parent=True) #set relationship databases
    market = db.relationship("Market", uselist=False, back_populates="users", cascade="all, delete-orphan", single_parent=True)
    notes = db.relationship("Note", uselist=False, back_populates="users", cascade="all, delete-orphan", single_parent=True)

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
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = db.relationship("User", back_populates="rent", single_parent=True, cascade="all, delete-orphan")

""" models for market database """

class Market(db.Model):
    __tablename__ = "market"
    id = db.Column(db.Integer, primary_key=True)
    market = db.Column(db.Integer)
    market_list = db.Column(db.String(1000))
    date = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = db.relationship("User", back_populates="market", single_parent=True, cascade="all, delete-orphan")

""" models for reminders notes """

class Note(db.Model):
    __tablename__ = "notes"
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.String(200))
    setDate = db.Column(db.DateTime(timezone=True))
    creationDate = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    users = db.relationship("User", back_populates="notes", single_parent=True, cascade="all, delete-orphan")