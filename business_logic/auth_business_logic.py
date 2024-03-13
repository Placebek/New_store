from models import user
import re


class AuthBusinessLogic:
    def __init__(self) -> None:
        pass

    def login_user(self, login, password):
        data_validated = False
        login_success = False

        user_login_pattern = r'^[a-zA-Z0-9_-]{3,16}$'
        user_password_pattern = r'^[a-zA-Z0-9_-]{3,16}$'

        if re.match(user_login_pattern, login) == False and re.match(user_password_pattern, password) == False:
            return login_success

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
