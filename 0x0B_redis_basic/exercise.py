#!/usr/bin/env python3
""" Redis exercise file """


import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Count calls decorator """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """ Cache class """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Store data in redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str,
                                                                    bytes,
                                                                    int,
                                                                    float]:
        """ Get data from redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Get string data from redis """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Get int data from redis """
        return self.get(key, int)
