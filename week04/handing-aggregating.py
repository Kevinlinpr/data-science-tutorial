import pandas as pd

data = {'Animal':
            ['Falcon','Falcon','Parrot','Parrot'],
        'Max Speed':
            [380.,60,90,100],
        'age':
            [10,7,9,20]
        }
df = pd.DataFrame(data)
print('===fundamental data===')
print(df)

top_data = df.head(n=3)
print('===Top Three order data')
print(top_data)

animal_group = df.groupby(['Animal'])
print('===Result of Group by Animal===')
print(animal_group.mean())

sum_age = animal_group.sum()['age']
print('===Amount of the Animal age===')
print(sum_age)

print('===type of the animal_group===')
print(type(animal_group))

print('===animal groups===')
print(animal_group.groups)

print('===dict keys of animal group===')
print(animal_group.groups.keys())

#there are still some problem with reorder the dataset