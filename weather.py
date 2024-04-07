import requests

api_key='enter your api key from accuweather.com'
city=input('Enter the city name :- ')

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    outlook = weather_data.json()['weather'][0]['main'] #selecting the correct array which gives the outlook
    temp = (weather_data.json()['main']['temp'])   #selecting the correct array for temprature
    cel=round((temp-32)*5/9, 2)     #to convert Fahrenheit in Celsius 

    print(f"The weather in {city} : {outlook}")
    print(f"The temperature in {city} is {cel}ºC")


