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
    date.run()