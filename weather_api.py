# weather_api.py

import requests
from config import WEATHER_API_KEY

def get_weather(city: str) -> str:
    """Получает информацию о погоде из OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]['description']
        temperature = main['temp']
        feels_like = main['feels_like']
        humidity = main['humidity']
        return (f"Погода в {city.capitalize()}:\n"
                f"Температура: {temperature}°C\n"
                f"Ощущается как: {feels_like}°C\n"
                f"Описание: {weather.capitalize()}\n"
                f"Влажность: {humidity}%")
    else:
        return "Город не найден. Пожалуйста, проверьте название и попробуйте снова."
