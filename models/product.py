from data_accessor import DataAccessor


class Product:
    """
        Өнімдер кестесінің моделі
    """
    def __init__(self, name=None, price=None, quantity=None, description=None,):
        self.data_accessor = DataAccessor()
        self.table_name = "products"

        self.columns_values = {
            "name": name,
            "price": price,
            "quantity": quantity,
            "description": description,
        }

    def create_product(self):
        self.data_accessor.insert_data(
            table_name=self.table_name,
            data=self.columns_values
        )

    def init_table(self):
        self.data_accessor.create_table(
            table_name=self.table_name,
            columns = ('id Serial Primary key, name varchar(50), price float, quantity int, description text'),
        )
