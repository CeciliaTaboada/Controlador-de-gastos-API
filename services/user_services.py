from models.db_models import User

class UserServices():

    def get_mail(email):
        return User.query.filter_by(email=email).first()

    def check_password(password, password1):
        if len(password) >= 8 and password == password1:
            return True