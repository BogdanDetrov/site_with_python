import requests


def weather_by_city():
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"

    params = {
        "key": "c46049cbb7e04385a7870147200105",
        "q": city_name,
        "format": "json",
        "num_of_days": 1,
        "lang": "ru"
    }
    try:
        result = requests.get(weather_url, params=params)
        weather = result.json()
        if "data" in weather:
            if "current_condition" in weather["data"]:
                try:
                    return weather["data"]["current_condition"][0]
    except(IndexError, TypeError):
        return False
    return False


if __name__ == "__main__":
    print(weather_by_city("Vladivostok"))
