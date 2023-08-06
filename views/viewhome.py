from flask import render_template, Blueprint
from flask_login import login_required

views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html")