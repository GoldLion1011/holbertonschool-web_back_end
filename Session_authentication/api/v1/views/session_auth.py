#!/usr/bin/env python3
""" Module that handles all routes for the Session Auth """

from api.v1.views import app_views
from flask import abort, jsonify, request
from models.user import User
from os import getenv


def get_user_from_session(session_id):
    """ Retrieves the user associated with a session """
    from api.v1.app import auth
    user_id = auth.get_user_from_session_id(session_id)
    if not user_id:
        return None
    user = User.get(user_id)
    return user


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /api/v1/auth_session/login
    Return:
      - User instance JSON represented
    """
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400
    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400
    try:
        user = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404
    if not user:
        return jsonify({"error": "no user found for this email"}), 404
    user = user[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    SESSION_NAME = getenv('SESSION_NAME')
    response = jsonify(user.to_json())
    response.set_cookie(SESSION_NAME, session_id)
    return response


@app_views.route('/users/me', methods=['GET'], strict_slashes=False)
def get_current_user():
    """ GET /api/v1/users/me
    Return:
      - User instance JSON represented
    """
    session_id = request.cookies.get('SESSION_NAME')
    if not session_id:
        return jsonify({"error": "unauthorized"}), 401

    user = get_user_from_session(session_id)
    if not user:
        return jsonify({"error": "unauthorized"}), 401

    return jsonify(user.to_json())
