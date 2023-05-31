#!/usr/bin/env python3
""" Basic Flask Module """

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")  # Flask app instance created, URL = /
def welcome():
    """ Welcome Method """
    return jsonify({"message": "Bienvenue"})  # JSON response via GET request


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
