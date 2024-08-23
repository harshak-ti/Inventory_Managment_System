import sqlite3

class File_Handler:
    def __init__(self, file):
        self.connection = sqlite3.connect(file)
        self.cursor = self.connection.cursor()

    def create_table(self, table_name, fields):
        # Dynamically create the SQL query to create a table
        fields_query = ", ".join(fields)
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({fields_query});"
        self.cursor.execute(query)
        self.connection.commit()

    def insert_value(self, table_name, data):
        # Prepare placeholders for the number of fields
        placeholders = ", ".join(["?"] * len(data))
        query = f"INSERT INTO {table_name} VALUES ({placeholders});"
        self.cursor.execute(query, data)
        self.connection.commit()

    def fetch_all(self, table_name):
        query = f"SELECT * FROM {table_name};"
        self.cursor.execute(query)
        return self.cursor.fetchall()
    
    def update_value(self, table_name, product_sku, field, new_value):
        query = f"UPDATE {table_name} SET {field} = ? WHERE Product SKU = ?;"
        self.cursor.execute(query, (new_value, product_sku))
        self.connection.commit()

    def delete_value(self, table_name, product_sku):
        query = f"DELETE FROM {table_name} WHERE Product SKU = ?;"
        self.cursor.execute(query, (product_sku,))
        self.connection.commit()

    def sort_products(self, table_name, sort_by, ascending=True):
        order = "ASC" if ascending else "DESC"
        query = f"SELECT * FROM {table_name} ORDER BY {sort_by} {order};"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def search_products(self, table_name, search_field, search_value):
        query = f"SELECT * FROM {table_name} WHERE {search_field} LIKE ?;"
        self.cursor.execute(query, (f"%{search_value}%",))
        return self.cursor.fetchall()

    def total_number_of_products(self, table_name):
        query = f"SELECT COUNT(*) FROM {table_name};"
        self.cursor.execute(query)
        return self.cursor.fetchone()[0]

    def close_connection(self):
        self.connection.close()