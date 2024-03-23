"""
    Базадағы кестелерді құратын файл
"""

import user, product

user_object = user.User()
user_object.drop_table()
user_object.init_table()

product_object = product.Product()

product_object.init_table()
