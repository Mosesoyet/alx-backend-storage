#!/usr/bin/env python3
"""
redis basic's module
"""
import redis
import uuid
from typing import Union, Callable, Optional


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


    def get_int(self, key: str) -> int:
        """
        Get data as integer from redis
        """
        data = self.get(key, lambda x: x.decode('utf-8'))
        data = int(data)
        return data
