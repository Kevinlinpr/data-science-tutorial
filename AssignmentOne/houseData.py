import sqlite3
import os.path

PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
print(PROJECT_ROOT)
house_database_file_path = os.path.join(PROJECT_ROOT,"data/housing.db")
house_data_sql_connect = sqlite3.connect(house_database_file_path)


