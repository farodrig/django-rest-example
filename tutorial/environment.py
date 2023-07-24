import distutils
import os
from typing import Any

from dotenv import dotenv_values
from yarl import URL


class Env:
    env: dict[str, Any]
    def __init__(self) -> None:
        self.env = dotenv_values() | os.environ  # override loaded values with environment variables

    def get(self, key: str):
        return self.env.get(key)

    def get_as_boolean(self, key: str) -> bool | None:
        value = self.get(key)
        return bool(distutils.util.strtobool(str(value))) if value else value
    
    def get_as_url(self, key: str) -> URL | None:
        value = self.get(key)
        return URL(value) if value else value
    
    def get_as_list(self, key: str) -> list | None:
        value = self.get(key)
        return list(map(lambda s: s.strip(), str(value).split(","))) if value else value

    
env = Env()