#!/usr/bin/env python3
"""
redis basic's module
"""
import redis
import uuid
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
    Count the number of times a function is called
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper func for the decorator
        """
        key = method.__qualname__
        self.redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Counts the No of times a function is called
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        wrapper function
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(method: Callable) -> None:
    """
    Replays to history of functions
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'), o.decode('utf-8')))


class Cache:
    """
    A class that store redis clients data
    """
    def __init__(self):
        """
        store _redis as a private attribute
        """
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        generates a random string key (e.g using uuid), store the input in Redis
        using the random key and return key
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key


    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Union[str, bytes, int, float, None]:
        """
        Get data from redis Cache
        """
        if data is not None and fn is not None and callable(fn):
            return fn(data)
        return data


    def get_str(self, key: str) -> str:
        """
        Get data as string from redis Cache
        """
        data = self.get(key, lambda x: x.decode('utf-8'))
        return data


    def get_int(self, key: int) -> int:
        """
        Get data as integer from redis
        """
        data = self.get(key, lambda x: int(x).decode('utf-8'))
        return data
