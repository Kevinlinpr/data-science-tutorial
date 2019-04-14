from AssignmentOne import Requirements as rq
from AssignmentOne.houseData import house_data_sql_connect
import pandas as pd
import matplotlib.pyplot as plt
# house area order
housing_area_df = pd.read_sql(rq.Requirements.Question_1_House_Area_SQL,house_data_sql_connect)
house_area_price = housing_area_df['sale price'].values
house_area = housing_area_df['house area'].values
# ground living area order
housing_area_df = pd.read_sql(rq.Requirements.Question_1_Living_Area_SQL,house_data_sql_connect)
living_area_price = housing_area_df['sale price'].values
living_area = housing_area_df['ground living area'].values
# basement size order
housing_area_df = pd.read_sql(rq.Requirements.Question_1_Basement_Size_SQL,house_data_sql_connect)
basement_size_price = housing_area_df['sale price'].values
basement_size = housing_area_df['basement size'].values


# basement_size = limit_housing_df['basement size'].values
# ground_living_area = limit_housing_df['ground living area'].values
# age_of_the_house = limit_housing_df['age of the house'].values

plt.ylim(0,housing_area_df['sale price'].max()+10000)
plt.xlim(0,housing_area_df['house area'].max()+1000)
plt.ylabel('Sale Price($)')
plt.xlabel('Area(in square feet)')
plt.title('House Area - Sale Price')
plt.plot(house_area,house_area_price)
plt.plot(living_area,living_area_price)
plt.plot(basement_size,basement_size_price)
Gender=['house area','ground living area','basement area']
plt.legend(Gender,loc=4)
plt.show()