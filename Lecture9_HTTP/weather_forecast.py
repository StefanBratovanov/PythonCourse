import requests
from datetime import datetime, timezone

city = input('Въведете град: ')
print('Обработваме заявката...')
appid = '965acdac1ae64cf06761bb563ad34d96'

resp = requests.get('http://api.openweathermap.org/data/2.5/weather', params={'q': city, 'appid': appid})
weather_info = resp.json()
print(weather_info)
date_of_measurement = datetime.fromtimestamp(weather_info['dt'], tz=timezone.utc)
temperature = float(weather_info['main']['temp']) / 273.15
pressure = weather_info['main']['pressure']
humidity = weather_info['main']['humidity']
wind = weather_info['wind']['speed']
print("""
Информация към: {date_of_measurement}
Температура: {temperature:.2f}
Налягане: {pressure}
Влажност: {humidity}%
Вятър: {wind} м/с
""".format(
        date_of_measurement=date_of_measurement.strftime("%Y-%m-%d %H:%M"),
        temperature=temperature,
        pressure=pressure,
        humidity=humidity,
        wind=wind,
))

# http://api.openweathermap.org/data/2.5/weather?q=sofia&appid=965acdac1ae64cf06761bb563ad34d96
