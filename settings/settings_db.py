from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import environ

db = SQLAlchemy()
dbconn = environ.get("sql_alchemy_conn")

def create_app():
    app = Flask("Control-de-gastos", template_folder="../Controlador-de-gastos-web/templates", static_folder="..\Controlador-de-gastos-web\static")
    app.config["SECRET_KEY"] = "SECRET_KEY"
    app.config["SQLALCHEMY_DATABASE_URI"] = dbconn
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from models.db_models import User, Rent, Market

    with app.app_context():
        db.create_all()
    
    return app
