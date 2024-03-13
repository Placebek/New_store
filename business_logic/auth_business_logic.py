
from models import user
from .patterns import validate_password, validate_login


class AuthBusinessLogic:
    def __init__(self) -> None:
        pass

    def login_user(self, login, password):
       
        if validate_login(login) and validate_password(password):
            login_success = True

        user_object = user.User()
        logged_in_user = user_object.get_user(
            ["id"], condition={
                "login": login,
                "password": password,
            }
        )

        if logged_in_user != []:
            # logged_in_user=('1', 'asd', 'asd', 'first_name', 'last_name')
            login_success = True

        return login_success

    def register_user(self, login, password, first_name, last_name):
        pass
