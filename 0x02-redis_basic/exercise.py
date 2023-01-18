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
