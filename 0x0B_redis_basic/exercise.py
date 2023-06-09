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


def call_history(method: Callable) -> Callable:
    """ Call history decorator """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)

        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)

        return output
    return wrapper


def replay(method: Callable):
    """ Replay decorator """
    r = redis.Redis()
    method_name = method.__qualname__
    count = r.get(method_name).decode("utf-8")
    inputs = r.lrange(method_name + ":inputs", 0, -1)
    outputs = r.lrange(method_name + ":outputs", 0, -1)

    print("{} was called {} times:".format(method_name, count))

    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(method_name, i.decode("utf-8"),
                                     o.decode("utf-8")))


class Cache():
    """ Cache class """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
