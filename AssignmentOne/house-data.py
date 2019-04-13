import sqlite3
import os.path
import pandas as pd

# obtain the housing.db real path
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))
house_database_file_path = os.path.join(PROJECT_ROOT,"data/housing.db")

house_data_sql_connect = sqlite3.connect(house_database_file_path)

ALL_TABLES_IN_HOUSING_DB_SQL_REQUEST = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
housing_df = pd.read_sql(ALL_TABLES_IN_HOUSING_DB_SQL_REQUEST,house_data_sql_connect)
print(housing_df.head())


