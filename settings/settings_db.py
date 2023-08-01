from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from os import environ

db = SQLAlchemy()
dbconn = environ.get("sql_alchemy_conn")

def create_app():
    app = Flask("Control-de-gastos", template_folder="../Controlador-de-gastos-web/templates", static_folder="..\Controlador-de-gastos-web\static")
    app.config["SECRET_KEY"] = "SECRET_KEY"
    app.config["SQLALCHEMY_DATABASE_URI"] = dbconn
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    from views.viewhome import views

    with app.app_context():
        app.register_blueprint(views, url_prefix="/")

    from models.db_models import User, Rent, Market, Note

    with app.app_context():
        db.create_all()

    log_man = LoginManager()
    log_man.login_view = "auth.login"
    log_man.init_app(app)
    
    @log_man.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app
