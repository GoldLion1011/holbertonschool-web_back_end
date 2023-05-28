#!/usr/bin/env python3
""" User module """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()  # Base class for SQLAlchemy model declaration


class User(Base):
    __tablename__ = 'users'  # MySQL table name

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
