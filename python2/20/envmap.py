import os
from cenviron import getenv, putenv

class EnvMapping:
    def __setitem__(self, key, value):
        os.environ[key] = value
        putenv(key, value)

    def __getitem__(self, key):
        value = getenv(key)
        os.environ[key] = value
        return value

Env = EnvMapping()