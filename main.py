from settings.settings_db import create_app
from services.user_services import UserServices

app = create_app()

@app.route("/", methods=["GET", "POST"])
def homepage():
    try:
        return UserServices.create_user()
    except:
        return UserServices.login()

