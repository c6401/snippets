from typing import TypedDict


class MyDict(TypedDict, total=False):
    name: str
