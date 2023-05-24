#!/usr/bin/env python3
""" Module of authentication views """

from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import List, TypeVar, Tuple
from models.user import User


class BasicAuth(Auth):
    """ API authentication class """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """ Method that returns None - authorization_header """
        if authorization_header is None or type(
                authorization_header) is not str:
            return None
        if authorization_header[0:6] != 'Basic ':
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                           str) -> str:
        """ Method that returns decoded value of
            base64_authorization_header """
        try:
            return b64decode(base64_authorization_header).decode('utf-8')
        except Exception:
            return None

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header:
                                 str) -> Tuple[str, str]:
        """ Method that user email and password
            for the Base64 decoded value """
        if decoded_base64_authorization_header is None or type(
                decoded_base64_authorization_header) is not str:
            return (None, None)
        if ':' not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(':', 1))

    def user_object_from_credentials(self, user_email:
                                     str, user_pwd: str) -> TypeVar('User'):
        """ Method that returns User instance based user_email and user_pwd """
        if user_email is None or type(user_email) is not str:
            return None
        if user_pwd is None or type(user_pwd) is not str:
            return None
        try:
            users = User.search({'email': user_email})
        except Exception:
            return None
        for user in users:
            if user.is_valid_password(user_pwd):
                return user
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """ Method that overloads Auth and retrieves
            the User instance for a request """
        auth_header = self.authorization_header(request)
        extract_header = self.extract_base64_authorization_header(auth_header)
        decode_header = self.decode_base64_authorization_header(extract_header)
        credentials = self.extract_user_credentials(decode_header)
        return self.user_object_from_credentials(credentials[0],
                                                 credentials[1])
