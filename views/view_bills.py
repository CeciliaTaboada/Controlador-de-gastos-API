from viewhome import views
from flask_login import login_required
from services.rent_services import RentServices

@views.route("/home", methods=["GET", "POST"])
def new_bill_payment():
    return RentServices.payment()

@views.route("/home/services", methods=["GET", "POST"])
def new_service_payment():
    return RentServices.services_payment()

@views.route("/home/all-bills")
def all_bills():
    return RentServices.check_bills()

@views.route("/home/latest-bill")
def last_bill():
    return RentServices.latest_bill()