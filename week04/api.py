import requests,json
import pandas as pd

api_key = '491a9ec8e8da3febdea1b7e83c2e9ed3'
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name: ")
url = base_url + "appid=" + api_key + "&q=" + city_name
response = requests.get(url)
x = response.json()
print('===print the response from the request===')
print(x)
temperature = x['main']['temp']
pressure = x['main']['pressure']
humidity = x['main']['humidity']
description = x['weather'][0]['description']

print('===using pandas===')
data={
    'attribute':['value'],
    'temperature':[temperature],
    'pressure':[pressure],
    'humidity':[humidity],
    'description':[description]
}
df = pd.DataFrame(data,columns=['attribute','temperature','pressure','humidity','description'])
print(df.head())