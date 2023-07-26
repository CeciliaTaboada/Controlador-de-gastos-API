from flask import request, flash, redirect
from flask_login import login_user
from werkzeug.security import check_password_hash
from services.user_services import UserServices

def login():
    if request.method == 'POST':
        email = request.form.get("email-login")
        password = request.form.get("password-login")

        usermail = UserServices.get_mail(email)
        
        if usermail:
            if check_password_hash(usermail.password, password):
                return login_user(usermail, remember=True)
            else:
                flash("Incorrect password", category="error")
        else:
            flash("Incorrect mail", category="error")
    return redirect("home.html")