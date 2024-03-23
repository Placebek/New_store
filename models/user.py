from models.data_accessor import DataAccessor


class User:
    """
        Қолданушылар кестесінің моделі
    """
    def __init__(self, email=None, phone_number=None, password=None):
        self.data_accessor = DataAccessor()
        self.table_name = "users"

        self.columns_values = {
            "email": email,
            "phone_number": phone_number,
            "password": password,
        
        }

    def create_user(self, data):
        register = self.data_accessor.insert_data(
            table_name="users",
            data=data
        )
        return register

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
            columns = ('id Serial Primary key, email varchar(100), phone_number int, password varchar(50)'),
        )
    
    def drop_table(self):
        self.data_accessor.drop_table(table_name=self.table_name)
