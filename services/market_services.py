from flask import request, render_template
from flask_login import current_user
from models.db_models import Market
from settings.settings_db import db

class MarketServices():

    @staticmethod
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
                total += price
                dic[stuff] = price

            mark = Market(market=total, market_list=dic)
            db.session.add(mark)
            db.session.commit()
        return render_template("home.html", user=current_user)
    
    @staticmethod
    def delivery():
        if request.method == 'POST':
            deli = request.form.get("delivery")

            new_deli = Market(delivery=deli)
            db.session.add(new_deli)
            db.session.commit()
        return render_template("home.html", user=current_user)
    
    @staticmethod
    def latest_market():
        return Market.query(Market.market).first()
    
    @staticmethod
    def all_market():
        dic = Market.query(Market.market_list).all()

        for _ in dic:
            for key, value in dic.items():
                """ create a function with a query to de dic  """
        pass