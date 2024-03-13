"""
    SQL-запростарды орындайтын файл
"""

import psycopg2
from psycopg2 import sql


class DataAccessor:
    def __init__(self, database='Hokken', user='postgres', password='duck1234', host='localhost', port='5432'):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port

        self.cursor = None
        self.conn = None

    def create_table(self, table_name, columns):
        self.__open_connection()
        print("DDDDD:", columns)

        sql_create_table = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns})'

        self.cursor = self.conn.cursor()

        self.cursor.execute(sql_create_table)
        self.conn.commit()
        self.__close_connection()

    def insert_data(self, table_name, data):
        self.__open_connection()
        columns = ', '.join(data.keys())
        values_template = ', '.join(['%s'] * len(data))
        sql_insert = sql.SQL(f'INSERT INTO {table_name} ({columns}) VALUES ({values_template})')
        
        self.cursor = self.conn.cursor()

        self.cursor.execute(sql_insert, list(data.values()))
        self.conn.commit()
        self.__close_connection()
    
    def drop_table(self, table_name):
        self.__open_connection()
        sql = f"DROP TABLE IF EXISTS {table_name}"

        self.cursor = self.conn.cursor()

        self.cursor.execute(sql)
        self.conn.commit()
        print(f"Table '{table_name}' dropped successfully.")
        self.__close_connection()

    def delete_data(self, table_name, condition):
        self.__open_connection()
        sql = f"DELETE FROM {table_name} WHERE {condition}"
        
        self.cursor = self.conn.cursor()

        self.cursor.execute(sql)

        self.conn.commit()
        print("Data deleted successfully.")
        self.__close_connection()

    def select_data(self, table_name, fields, condition):
        self.__open_connection()

        fields_string = ""

        for field in fields:
            fields_string += "%s, "%field

        fields_string = fields_string[:-2]

        if condition == None:
            sql = f"SELECT {fields_string} FROM {table_name}"
        else:
            where_string = ""
            for key, value in condition.items():
                if isinstance(value, str):
                    where_string += "%s = '%s' AND "%(key, value)

            if where_string.endswith(' AND '):
                where_string = where_string[:-5]

            sql = f"SELECT {fields_string} FROM {table_name} WHERE {where_string}"

            print("ЗАПРОС: ", sql)

        self.cursor = self.conn.cursor()

        self.cursor.execute(sql)

        table_data = self.cursor.fetchall()

        self.__close_connection()

        return table_data

    def __open_connection(self):
        self.conn = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def __close_connection(self):
        self.conn.close()

# class courses():
#     def courses():
#         conn = Dataaccessor()
#         conn.drop_table(courses) 
#         columns = ('course_id Serial Primary key, course_name character varying(100), course_code character varying(20)')
#         conn.create_table(columns=columns)

