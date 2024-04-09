"""
Returns the current date in the format "YYYY-MM-DD".
"""
"""
Provides a Flask API with three endpoints to retrieve the current date, day, and time.

The `get_current_date()` function returns the current date in the format "YYYY-MM-DD".

The `get_current_day()` function returns the current day of the week as a string (e.g. "Monday", "Tuesday", etc.).

The `get_current_time()` function returns the current time in the format "HH:MM:SS".
"""
from flask import Flask, jsonify
from datetime import datetime

date = Flask(__name__)


@date.route("/current_date", methods=["GET"])
def get_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return jsonify({"current_date": current_date})


@date.route("/current_day", methods=["GET"])
def get_current_day():
    current_day = datetime.now().strftime("%A")
    return jsonify({"current_day": current_day})


@date.route("/current_time", methods=["GET"])
def get_current_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    return jsonify({"current_time": current_time})


if __name__ == "__main__":
    date.run(port=5000)
