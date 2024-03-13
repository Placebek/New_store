from models.data_accessor import DataAccessor


class User:
    """
        Қолданушылар кестесінің моделі
    """
    def __init__(self, login=None, password=None, first_name=None, last_name=None):
        self.data_accessor = DataAccessor()
        self.table_name = "users"

        self.columns_values = {
            "login": login,
            "password": password,
            "first_name": first_name,
            "last_name": last_name,
        }

    def create_user(self):
        self.data_accessor.insert_data(
            table_name=self.table_name,
            data=self.columns_values
        )

    def get_user(self, fields, condition):
        selected_user = self.data_accessor.select_data(
            table_name=self.table_name,
            fields=fields,
            condition=condition
        )

        return selected_user

    def init_table(self):
        self.data_accessor.create_table(
            table_name=self.table_name,
            columns = ('id Serial Primary key, first_name varchar(50), last_name varchar(50), login varchar(50), password varchar(50)'),
        )
