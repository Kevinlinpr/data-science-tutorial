import pandas as pd
from AssignmentOne.houseData import house_data_sql_connect

ALL_TABLES_IN_HOUSING_DB_SQL_REQUEST = "SELECT [MS Zoning] , SalePrice FROM houses"
housing_df = pd.read_sql(ALL_TABLES_IN_HOUSING_DB_SQL_REQUEST,house_data_sql_connect)
print(housing_df.groupby(['MS Zoning']).mean())

'''
    MS Zoning      SalePrice
    A (agr)     13100.000000
    C (all)     84951.350000
    FV         218831.530973
    I (all)    103000.000000
    RH         138853.360000
    RL         191660.800330
    RM         127463.866120
'''
