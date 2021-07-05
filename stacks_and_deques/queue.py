from helpers.helpers import *


T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self):
        self._data: List[T] = []

    def push(self, item: T) -> None:
        self._data.append(item)

    def pop(self) -> T:
        return self._data.pop(0)

    def __len__(self):
        return len(self._data)

    def __str__(self):
        return str(self._data)

    def __repr__(self):
        return repr(self._data)

    def __ne__(self, other: int):
        return len(self._data) != other

    def check(self):
        return self._data[0]

