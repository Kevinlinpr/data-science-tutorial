import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {'Age': ['Young','Middle','Old'],
        'Male': [1783,2289,1032],
        'Female': [1950,2320,1491],
        'Total': [3733,4609,2523]
        }

df = pd.DataFrame(data,columns= ['Age', 'Male', 'Female','Total'])

df.head()

total = df['Total'].values
male = df['Male'].values
female = df['Female'].values
x_pos = np.arange(len(total))
# plt.bar(x_pos,total,align='center')
plt.bar(x_pos,female)
plt.bar(x_pos,male,bottom=female)

plt.xticks(x_pos,('Young','Middle','Old'))
plt.ylabel('Top Population')
plt.title('Population by Age Bracket')

Gender=['Female','Male']
plt.legend(Gender,loc=2)
plt.show()

bar_width = 0.35

plt.barh(x_pos,df['Male'].values, bar_width, color='blue')
plt.barh(x_pos+bar_width,df['Female'].values, bar_width, color='green')

# again we add labels and title
# notice that xticks is now yticks and ylabel is now xlabel
plt.yticks(x_pos+(bar_width/2), ('Young', 'Middle', 'Old'))
plt.xlabel('Total Population')
plt.title('Population by Age Bracket')

# we add a colour map
Gender=['Male','Female']
plt.legend(Gender,loc=1)
plt.show()

# del df['Total']
# df.plot(kind='bar',stacked=True)
# plt.show()