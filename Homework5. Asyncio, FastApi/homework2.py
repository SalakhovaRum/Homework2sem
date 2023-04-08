from fastapi import FastAPI

import requests

app = FastAPI()

API_key = "08df79a0cfb21ef760ec9e1ddc9dcea6"
base_url = "http://api.openweathermap.org/data/2.5/weather?"


@app.get("/weather/{city_name}")
async def get_weather(city_name: str):
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

    return {
        "city": city_name,
        "temperature": temp,
        "wind_speed": wind_speed,
        "description": description,
        "latitude": latitude,
        "longitude": longitude
    }
