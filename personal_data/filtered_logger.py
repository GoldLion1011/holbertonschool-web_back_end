#!/usr/bin/env python3
"""Regex-ing"""

import typing
import re
import logging


def filter_datum(fields: typing.List[str], redaction: str, message: str,
                 separator: str) -> str:
    """returns the log message obfuscated"""
    for field in fields:
        message = re.sub(f"{field}=.*?{separator}",
                         f"{field}={redaction}{separator}", message)
    return message
