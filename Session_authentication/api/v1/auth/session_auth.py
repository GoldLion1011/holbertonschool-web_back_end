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
