from flask import request, flash, render_template, redirect, url_for
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models.db_models import User
from settings.settings_db import db


class UserServices():


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
    
    @staticmethod
    def login():
        if request.method == 'POST':
            user = UserServices.get_mail(request.form.get("email-login"))
            
            if user:
                if check_password_hash(user.password, request.form.get("password-login")):
                    login_user(user, remember=True)
                    name = user.name
                    return redirect(url_for("views.home", name= name, user=current_user))
                else:
                    flash("Incorrect password", category="error")
            else:
                flash("Incorrect mail", category="error")
        return render_template("index.html", user = current_user)

    @staticmethod
    def get_mail(email):
        return User.query.filter_by(email=str(email)).first()

    @staticmethod
    def check_password(password, password1):
        if len(password) < 8 or password != password1:
            return False
        return True