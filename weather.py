import requests

api_key='130f9c1fcffb4ac7a6a65f33c07d6600'
city=input('Enter the city name :- ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    outlook = weather_data.json()['weather'][0]['main']
    temp = (weather_data.json()['main']['temp'])
    cel=round((temp-32)*5/9, 2)

    print(f"The weather in {city} : {outlook}")
    print(f"The temperature in {city} is {cel}ºC")


