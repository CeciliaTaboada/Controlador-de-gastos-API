from flask import request, render_template, flash,redirect, jsonify
from flask_login import login_user, current_user
from werkzeug.security import generate_password_hash
from routes.auth import auth
from models.db_models import User, db
from services.user_services import UserServices

@auth.route('/', methods=['GET', 'POST'])
def create_user():
    signup = request.form.args.get("signupform") #get signup form since login form its in the same html
    if signup and request.method == 'POST':
        email = request.form.get("email"), 
        password = request.form.get("password"), 
        password1 = request.form.get("password1"), 
        name = request.form.get("name") 

        user = UserServices.get_mail(email) #checks email in user database returns user if exists
        password_check = UserServices.check_password(password, password1) #checks password returns boolean

        if user:
            flash("Email already exists", category="error") #if user exist shows an error
        elif not password_check:
            flash("Password not valid", category="error") #if password len < 8 and/or password != password1 shows an error
        else:
            new_user = User(name=name, email=email, password=generate_password_hash(password, method="sha256")) #create new user under user database model
            db.session.add(new_user) #add new user to the database
            db.session.commit() #commit new user to the database
            login_user(new_user, remember=True) #keep the user loged in
    
    return jsonify(user=current_user) 