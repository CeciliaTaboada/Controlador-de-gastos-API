from viewhome import views
from flask_login import login_required
from services.market_services import MarketServices

@views.route("/home", methods=["GET", "POST"])
def new_shop():
    return MarketServices.new_market()

@views.route("/home/latest-shop")
def last_shop():
    return MarketServices.latest_market()

@views.route("/home/shop-list")
def shop_list():
    return MarketServices.all_market()