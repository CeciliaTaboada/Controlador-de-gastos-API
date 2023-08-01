from flask import request, render_template
from flask_login import current_user
from models.db_models import Rent
from settings.settings_db import db

class RentServices():

    @staticmethod
    def payment():
        if request.method == "POST":
            rent = request.form.get("bills-div")
            date = request.form.get("date")
            expenses = request.form.get("expenses")

            newpayment = Rent(rent=rent, date = date, expenses=expenses)
            db.session.add(newpayment)
            db.session.commit()
        return render_template("home.html", user=current_user)
    
    @staticmethod
    def services_payments():
        if request.method == "POST":
            electricity = request.form.get("electricity")
            gas = request.form.get("gas")
            water = request.form.get("water")

            services = Rent(electricity=electricity, gas=gas, water=water)
            db.session.add(services)
            db.session.commit()
        return render_template("home.html", user=current_user)
    
    @staticmethod
    def check_bills():
        return Rent.query(Rent.rent, Rent.expenses, Rent.electricity, Rent.gas, Rent.water).all()

    @staticmethod
    def latest_bill():
        return Rent.query(Rent.rent, Rent.expenses, Rent.electricity, Rent.gas, Rent.water).first()
