from main import app

class Settings():
    app.config["SQLALCHEMY_DATABASE_URI"] = "DATABASE"
    app.config["SECRET_KEY"] = "SECRET_KEY"

app_db = Settings()