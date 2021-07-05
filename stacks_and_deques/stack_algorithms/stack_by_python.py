from typing import List, TypeVar, Generic, Optional

T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._stack: List[Optional[T]] = []

    def pop(self) -> T:
        return self._stack.pop()

    def push(self, value: T):
        self._stack.append(value)

    def __str__(self):
        return str(self._stack)


if __name__ == '__main__':
    new = Stack()
    for i in range(5):
        new.push(i)
    print(new)
