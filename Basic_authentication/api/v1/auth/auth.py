#!/usr/bin/env python3
""" Module of authentication views """

from flask import request
from typing import List, TypeVar


class Auth():
    """ API authentication class """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Method that returns False - path and excluded_paths """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        if path in excluded_paths or path + '/' in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """ Method that returns None - request """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that returns None - request """
        return None
