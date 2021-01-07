from flask import Flask, render_template, request, redirect
from weather import get_weather

app = Flask(__name__)
city = None

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/", methods=["POST"])
def get_city():
    if request.method == "POST":
        city = request.form["text"]
        weather = get_weather(city)
        weatherinfo = None
        if not weather:
            weatherinfo = 'Could not retrieve info for given city. Check input.'
        else:
            weatherinfo = 'Current temperature for {} is {}. Feels like {}. {}'.format(city, weather[0], weather[1], weather[2])

    return render_template('home.html', result = weatherinfo)

@app.route("/forecast")
def forecast():
    return render_template('forecast.html')

@app.route("/forecast", methods=["POST"])
def get_forecast():
    return render_template("forecast.html", result = city)


if __name__ == "__main__":
    app.run(debug=True)
