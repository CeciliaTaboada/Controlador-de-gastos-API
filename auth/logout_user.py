from flask import redirect
from flask_login import login_required, logout_user
from routes.auth import auth

@auth.route("/home")
@login_required
def logout():
    logout_user()
    return redirect("/")