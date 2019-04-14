from AssignmentOne import Requirements as rq
from AssignmentOne.houseData import house_data_sql_connect
import pandas as pd

limit_housing_df = pd.read_sql(rq.Requirements.Question_1_adv_SQL,house_data_sql_connect)
house_mean = limit_housing_df.groupby(['type of dwelling','house style']).mean()
house_mean_df = pd.DataFrame(house_mean)
house_mean_df_round = house_mean_df.round({
    'rates overall condition':1,
    'age of the house':0,
    'ground living area':1,
    'basement size':1,
    'house area':1,
    'sale price':2
})
print(house_mean_df_round)