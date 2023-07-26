from models.db_models import User

class UserServices():

    @staticmethod
    def get_mail(email):
        return User.query.filter_by(email=str(email)).first()

    @staticmethod
    def check_password(password, password1):
        if len(password) < 8 or password != password1:
            return False
        return True