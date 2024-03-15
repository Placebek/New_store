from models import user
from .patterns import validate_password, validate_login, validate_name


class AuthBusinessLogic:
    def __init__(self) -> None:
        pass

    def login_user(self, login, password):
       
        if validate_login(login) and validate_password(password) :
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

        if validate_name(first_name) and validate_name(last_name):
            name_success = True

        user_object = user.User()
        register_in_user = user_object.create_user(
            ["id"], data={
                "login": login,
                "password": password,
                "first_name": first_name,
                "last_name": last_name
            }
        )

        if register_in_user != []:
            # logged_in_user=('1', 'asd', 'asd', 'first_name', 'last_name')
           name_success = True

        return name_success