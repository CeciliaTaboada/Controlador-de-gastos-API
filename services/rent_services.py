from flask import request, render_template
from flask_login import current_user
from models.db_models import Rent
from settings.settings_db import db
from sqlalchemy import asc

class RentServices():

    def payment():
        if request.method == "POST":
            rent = request.form.get("bills-div")
            date = request.form.get("date")
            expenses = request.form.get("expenses")

            newpayment = Rent(rent=rent, date = date, expenses=expenses, user_id=current_user.id)
            db.session.add(newpayment)
            db.session.commit()
        return render_template("home.html", user=current_user)
    
    def services_payments():
        if request.method == "POST":
            electricity = request.form.get("electricity")
            gas = request.form.get("gas")
            water = request.form.get("water")

            services = Rent(electricity=electricity, gas=gas, water=water, user_id=current_user.id)
            db.session.add(services)
            db.session.commit()
        return render_template("home.html", user=current_user)
    
    @staticmethod
    def check_bills():
        rent_bills = db.session.execute(db.select(Rent.rent, Rent.expenses, Rent.electricity, Rent.gas, Rent.water).where(Rent.user_id == current_user.id)).scalars()
        return rent_bills

    @staticmethod
    def latest_bill():
        last_bill = db.session.execute(db.select(Rent.rent, Rent.expenses, Rent.electricity, Rent.gas, Rent.water).order_by(asc(Rent.date)).where(Rent.user_id == current_user.id ))
        return last_bill
