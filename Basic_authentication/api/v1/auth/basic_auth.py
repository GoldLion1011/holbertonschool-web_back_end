#!/usr/bin/env python3
""" Module of authentication views """

from api.v1.auth.auth import Auth


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
                                            base64_authorization_header: str) -> str:
        """ Method that returns decoded value of
            base64_authorization_header """
        if base64_authorization_header is None or type(
                base64_authorization_header) is not str:
            return None
        try:
            return base64_authorization_header.decode('utf-8')
        except Exception:
            return None

