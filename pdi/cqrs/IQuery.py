from typing import Generic, TypeVar

from .CommandQueryBase import CommandQueryBase

Q = TypeVar('Q', covariant=True)


class IQuery(Generic[Q], CommandQueryBase[Q]):
    def __init__(self) -> Q:
        pass