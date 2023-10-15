from os import getenv
from typing import NoReturn, Self

__all__ = [
    "EnvUndefined",
    "StrEnv",
    "BoolEnv",
]


class EnvUndefined(Exception):
    """Raise when cannot read env variable and getenv return None"""

    def __init__(self, env_name: str) -> None:
        msg = f'Env name="{env_name}"'
        super().__init__(msg)


class StrEnv(str):
    def __new__(cls, env_name: str) -> Self | NoReturn:
        env = getenv(env_name, None)
        if env is None:
            raise EnvUndefined(env_name)
        obj = str.__new__(cls, env)
        return obj


class BoolEnv:
    def __new__(cls, env_name: str) -> bool | NoReturn:
        env = getenv(env_name, None)
        if env is None:
            raise EnvUndefined(env_name)
        return env.lower() in ("true", "1")
