from flask import redirect, url_for
from flask_login import login_required, logout_user
from views.viewhome import views

@views.route("/home")
@login_required
def logout():
    logout_user()
    return redirect(url_for("app.homepage"))