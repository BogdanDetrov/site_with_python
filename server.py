from flask import Flask
from weather import weather_by_city

app = Flask(__name__)


@app.route('/')
def hello():
    weather = weather_by_city("Vladivostok")
    if weather:
        weather_text = return f"Погода: {weather['temp_C']}, ощущается как {weather['FeelsLikeC']}."
    else:
        weather_text = 'Сервис погоды временно недоступен.'


if __name__ == "__main__":
    app.run(debug=True)
