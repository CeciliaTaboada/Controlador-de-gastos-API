from flask import render_template
from auth.new_user import create_user
from auth.login_user import login
from settings.settings_db import create_app

app = create_app()

@app.route("/", methods=["GET", "POST"])
def homepage():
    try:
        create_user()
    except:
        login()
    finally:
        return render_template("index.html")

