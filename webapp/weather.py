from flask import current_app
import requests

def weather_by_city(city_name):
    '''Принимает на вход название города и выдаёт в формате json результат'''
    weather_url = current_app.config["URLS"]
    params = {
        "key": current_app.config["WEATHER_API_KEY"],
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:  
        result = requests.get(weather_url, params=params)
        # raise_for_status() формирует исключения если сервер ответит кодом 4.. 5..
        result.raise_for_status()
        # мы получим в виде строки а нам надо в формате json, преобразуем
        weather = result.json()


        # добавим проверку наличия секции 'data'
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        # отслеживаем ошибки и исключения
        print('Сетевая ошибка')
        return False
    return False

# если вызвать код на прямую что бы он отработал
if __name__ == "__main__":
    print(weather_by_city("Moscow,Russia"))
