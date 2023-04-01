import requests

API_key = "08df79a0cfb21ef760ec9e1ddc9dcea6"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

city_name = input("Enter City Name : ")

Final_url = base_url + "appid=" + API_key + "&q=" + city_name
weather_data = requests.get(Final_url).json()

# Получаем доступ к температуре
temp = weather_data['main']['temp']

# Получаем доступ к ветру
wind_speed = weather_data['wind']['speed']

# Получаем доступ к описанию
description = weather_data['weather'][0]['description']

# Получаем доступ к широте
latitude = weather_data['coord']['lat']

# Получаем доступ к долготе
longitude = weather_data['coord']['lon']


print('\nТемпература : ', temp)
print('\nСкорость ветра : ', wind_speed)
print('\nОписание : ', description)
print('\nШирота : ', latitude)
print('\nДолгота : ', longitude)
