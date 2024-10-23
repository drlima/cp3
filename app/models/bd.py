from typing import TypedDict
from .auth import Authentication
from .user import User


class BD(TypedDict):
    auth: list[Authentication]
    users: list[User]


# singleton
bd = BD(auth=[], users=[])
