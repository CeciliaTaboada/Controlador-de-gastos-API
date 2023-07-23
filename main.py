from flask import render_template, request
from auth.new_user import create_user
from auth.login_user import login
from settings.settings_db import create_app

app = create_app()

@app.route("/", methods=["GET", "POST"])
def homepage():
    user_up = create_user()
    return render_template("index.html", user=user_up)
