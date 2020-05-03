from flask import Flask, render_template
from weather import weather_by_city
from news_python import get_python_news

app = Flask(__name__)

@app.route('/')
def hello():
    title = 'Новости Python'
    weather = weather_by_city("Vladivostok")
    news_list = get_python_news()
    return render_template("index.html", page_title=title, weather=weather, news=news_list)

if __name__ == "__main__":
    app.run(debug=True)