#!/usr/bin/env python3
"""Regex-ing"""

from typing import List
import re
import logging
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Redacting Formatter class """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        """ Filter values in incoming log """
        msg = super().format(record)
        return filter_datum(self.fields, self.REDACTION, msg, self.SEPARATOR)


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message


def get_logger() -> logging.Logger:
    """returns a logging.Logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    connector = mysql.connector.connect(
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_PASSWORD', ''),
        host=os.getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.getenv('PERSONAL_DATA_DB_NAME'))
    return connector


def main():
    """main function"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    logger = get_logger()
    for row in cursor:
        message = "name={}; email={}; phone={}; ssn={}; password={}; \
                    ip={}; last_login={}; user_agent={}; ".format(
                    row[0], row[1], row[2], row[3], row[4], row[5],
                    row[6], row[7])
        logger.info(message)
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
