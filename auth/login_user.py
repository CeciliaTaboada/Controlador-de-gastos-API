from flask import request, flash, redirect, render_template, url_for
from flask_login import login_user, current_user
from werkzeug.security import check_password_hash
from services.user_services import UserServices

def login():
    if request.method == 'POST':
        email = request.form.get("email-login")
        password = request.form.get("password-login")

        usermail = UserServices.get_mail(email)
        
        if usermail:
            if check_password_hash(usermail.password, password):
                login_user(usermail, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Incorrect mail", category="error")
    return render_template("index.html", user = current_user)