#!/usr/bin/env python3
""" Auth module """


from bcrypt import hashpw, gensalt, checkpw
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Register a user """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

    def valid_login(self, email: str, password: str) -> bool:
        """ Check if a user exists and the password is valid """
        try:
            user = self._db.find_user_by(email=email)
            return checkpw(password.encode(), user.hashed_password)
        except NoResultFound:
            return False


def _hash_password(password: str) -> str:
    """ A salted hash of the input password, hashed with bcrypt.hashpw """
    return hashpw(password.encode(), gensalt())


def _generate_uuid(self) -> str:
    """ Generate a UUID """
    return str(uuid.uuid4())
