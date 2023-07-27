from flask import request, flash, render_template, redirect, url_for
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash
from models.db_models import User
from settings.settings_db import db
from services.user_services import UserServices

def create_user():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        password1 = request.form.get("password1")
        name = request.form.get("name")

        usermail = UserServices.get_mail(email) #checks email in user database returns user if exists
        password_check = UserServices.check_password(password, password1) #checks password returns boolean

        if usermail:
            raise flash("User already exists")
        if not password_check:
            raise flash("Password not valid or not the same")
    
        newuser = User(name=name, email=email, password=generate_password_hash(password, method="scrypt")) #create new user under user database model
        db.session.add(newuser)
        try:
            db.session.commit()
            login_user(newuser, remember=True) #keep the user loged in
        except:
            db.session.rollback()
        return redirect(url_for("views.home"))
    return render_template("index.html", user = current_user)
    