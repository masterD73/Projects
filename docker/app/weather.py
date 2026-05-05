# ------------------
# title: Weather App
# ------------------
# -----------------------
# Description:
# Gotta predict them all.
# -----------------------
# ----------------------------
# Author: Daniel Merchav.
# Reviewer: Daniel Braunstein.
# AI2 InfinityLabs.
# ----------------------------
import json  # To load JSON data to a python dictionary.
import urllib.request  # urllib.request to make a request to api.
from xmlrpc.client import SERVER_ERROR  # Server Error
from api_code import api_key  # API key
from datetime import date as dt  # To calculate appropriate day name.
from flask import Flask, render_template, request  # To render the HTML and run a website.

YEAR, MONTH, DAY = 0, 1, 2
app = Flask(__name__)


def k_to_c(num: float | int, rounded=2) -> float:
    """
    Transform Kelvin temperature to Celsius.
    :param num: Kelvin degrees.
    :param rounded: Optional rounding variable.
    :return: float
    """
    k_const = 273.15
    return round(num - k_const, rounded)


def check_code(code: str) -> None:
    """
    Check code received from server.
    Raise error when possible.
    :param code: Code to be matched.
    :return: None
    """
    match code:
        case "300":
            raise Exception("Redirection error")
        case "404":
            raise ValueError("City not found")
        case "500":
            raise SERVER_ERROR


@app.route('/', methods=['POST', 'GET'])
def weather():
    if request.method == 'POST':
        city = request.form['city']
    else:
        city = 'jerusalem'

    first_dict = 0
    api = api_key
    city = city.replace(" ", "%20")

    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&format=json"
    try:
        geo = urllib.request.urlopen(geo_url).read()
        geo_data = json.loads(geo)
        if "results" not in geo_data:
            raise ValueError("Invalid city")
        source_url = (f'http://api.openweathermap.org/data/2.5/forecast?lat='
                      f'{float(geo_data["results"][first_dict]["latitude"])}&lon='
                      f'{float(geo_data["results"][first_dict]["longitude"])}&appid={api}')
        source = urllib.request.urlopen(source_url).read()
        list_of_data = json.loads(source)
        check_code(list_of_data["cod"])
        temperature, data = {}, {}
        for info in list_of_data["list"]:
            date, time = info["dt_txt"].split()
            day = date.split("-")
            day = dt(int(day[YEAR]), int(day[MONTH]), int(day[DAY])).strftime("%A")
            if date not in data:
                data[date] = {"Day": day, "Date": date}
            if time == "09:00:00":
                data[date]["morning_temp"] = str(k_to_c(info["main"]["temp"])) + "°C"
                data[date]["morning_humid"] = str(info["main"]["humidity"]) + "%"
            elif time == "21:00:00":
                data[date]["night_temp"] = str(k_to_c(info["main"]["temp"])) + "°C"
                data[date]["night_humid"] = str(info["main"]["humidity"]) + "%"
        location = [geo_data["results"][first_dict]["name"], geo_data["results"][first_dict]["country"]]
        data = list(data.values())
        print(data)
        print(temperature)
        print(location)
        return render_template('index.html', data=data, location=location)
    except Exception as e:
        error_message = e
        return render_template('index.html', error=error_message)


if __name__ == '__main__':
    app.run(debug=True)
