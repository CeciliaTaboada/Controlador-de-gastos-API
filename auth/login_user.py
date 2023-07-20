from flask import request, flash, render_template
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash
from routes.auth import auth
from services.user_services import UserServices

@auth.route('/', methods=['GET', 'POST'])
def login():
    login = request.form.args.get("loginform")
    if login and request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")

        user = UserServices.get_mail(email)

        if user:
            if check_password_hash(user.password, password):
                return login_user(user, remember=True)
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Incorrect mail", category="error")
    return render_template("home.html", user=current_user)