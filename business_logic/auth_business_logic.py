from models import user
from .patterns import validate_password, validate_login, validate_phone_number


class AuthBusinessLogic:
    def __init__(self) -> None:
        pass

    def login_user(self, email, password):
       
        if validate_login(email) and validate_password(password) :
            login_success = True
        else:
            login_success = False

        user_object = user.User()
        logged_in_user = user_object.get_user(
            ["*"], condition={
                "email": email,
                "password": password,
            }
        )

        if logged_in_user != []:
            # logged_in_user=('1', 'asd', 'asd', 'first_name', 'last_name')
            login_success = True

        return login_success

    def register_user(self, email, phone_number, password):
        name_success = False

        if validate_phone_number(phone_number):
            name_success = True

            data = {
                "email": email,
                "phone_number": phone_number,
                "password": password,
            }

            user_object = user.User()
            register_in_user = user_object.create_user(data=data)

            if register_in_user is not None:
                name_success = True

        return name_success


    def auth_user(self, email, password):
        auth_success = False

        
        user_object = user.User()
        logged_in_user = user_object.get_user(
            ["*"], condition={
                "email": email,
                "password": password,
            }
        )

        if logged_in_user != []:
            auth_success = True

        return auth_success