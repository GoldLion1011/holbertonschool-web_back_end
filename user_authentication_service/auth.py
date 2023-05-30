#!/usr/bin/env python3
""" Auth module """


from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> str:
    """ A salted hash of the input password, hashed with bcrypt.hashpw """
    return hashpw(password.encode(), gensalt())
