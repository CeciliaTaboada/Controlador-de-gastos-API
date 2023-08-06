from flask import request, render_template
from flask_login import current_user
from models.db_models import Market
from settings.settings_db import db
from sqlalchemy import asc
import pandas as pd

class MarketServices():

    def new_market():
        if request.method == 'POST':
            dic = {}
            total = 0
            """ create a form with a key and a value """
            """ add a counter to the form on the items """
            lenght = request.form.get("count")
            for _ in range(1, lenght):
                stuff = request.form.get("stuff")
                price = request.form.get("price")
                total += int(price)
                dic[stuff] = price

            mark = Market(market=total, market_list=dic, user_id=current_user.id)
            db.session.add(mark)
            db.session.commit()
        return render_template("home.html", user=current_user)
        
    @staticmethod
    def latest_market():
        return db.session.execute(db.select(Market.market).order_by(asc(Market.date))).first()
    
    @staticmethod
    def all_market():
        dic = db.session.execute(db.select(Market.market_list))
        date = db.session.execute(db.select(Market.date))
        data_m = []
        date_m = []
        for _ in date:
            for key, value in dic.items():
                data_m.append({key: value})
            date_m.append(data_m)
        return pd.DataFrame(date_m)