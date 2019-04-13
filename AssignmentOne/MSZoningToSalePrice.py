import pandas as pd
from AssignmentOne.houseData import house_data_sql_connect

ALL_TABLES_IN_HOUSING_DB_SQL_REQUEST = "SELECT [MS Zoning] , SalePrice FROM houses"
housing_df = pd.read_sql(ALL_TABLES_IN_HOUSING_DB_SQL_REQUEST,house_data_sql_connect)
print(housing_df.groupby(['MS Zoning']).mean())
