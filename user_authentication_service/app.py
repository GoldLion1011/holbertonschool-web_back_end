#!/usr/bin/env python3
""" Basic Flask Module """

from flask import Flask, jsonify, request
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route("/")  # Flask app instance created, URL = /
def welcome():
    """ Welcome Method """
    return jsonify({"message": "Bienvenue"})  # JSON response via GET request


@app.route("/users", methods=["POST"])
def users():
    """ User registration route """
    email = request.form.get("email")
    password = request.form.get("password")
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
