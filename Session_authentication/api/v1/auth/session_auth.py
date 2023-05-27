#!/usr/bin/env python3
""" Module of session auth """

from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """ Class of session auth """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """ Method that create a session ID for a user_id """
        if user_id is None or type(user_id) != str:
            return None
        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """ Method that return a User ID based on a Session ID """
        if session_id is None or type(session_id) != str:
            return None
        session_id = self.user_id_by_session_id.get(session_id)
        return session_id

    def current_user(self, request=None):
        """ Method that return a User instance based on a cookie value """
        session_cookie = self.session_cookie(request)
        user_id = self.user_id_for_session_id(session_cookie)
        from models import User
        return User.get(user_id)
