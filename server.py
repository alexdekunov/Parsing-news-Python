from flask import Flask, render_template
from weather import weather_by_city

app = Flask(__name__)

@app.route('/')
def index():
    title = "прогноз погоды"
    weather = weather_by_city("Moscowweather_by_city,Russia")
    if weather:
        weather_text = f"Погода: {weather['temp_C']} градусов, ощущется как: {weather['FeelsLikeF']} градусов"
    else:
        weather_text = "Сервис погоды временно не доступен"
    return render_template('index.html', page_title=title, weather=weather_text )

if __name__ == "__main__":
    app.run(debug=True)