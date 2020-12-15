import requests
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        city = request.form["cty"]
        return redirect(url_for("city", cty=city))
    else:
        return render_template("index.html")

@app.route("/<cty>")
def city(cty):
    try:
        weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid=5f56ae6cc57e0405f2b0a55b5edf8536".format(
            cty)
        r = requests.get(weather_url)
        data = r.json()
        status = data["weather"][0]["main"]
        if status == "Clouds":
            return redirect(url_for("clouds"))
        elif status == "Clear":
            return redirect(url_for("clear"))
        elif status == "Thunderstorm":
            return redirect(url_for("thunderstorm"))
        else:
            return redirect(url_for("home"))
    except KeyError:
        return redirect(url_for("home"))

@app.route("/Clouds")
def clouds():
    return render_template("jalter.html")

@app.route("/Clear")
def clear():
    return render_template("quetz.html")

@app.route("/Thunderstorm")
def thunderstorm():
    return render_template("ivan.html")

@app.route("/Drizzle")
def drizzle():
    return render_template("tesla.html")

if __name__ == "__main__":
    app.run()