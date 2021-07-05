from abc import abstractmethod, ABC
from typing import TypeVar, Generic, Optional, List


T = TypeVar('T')
N = TypeVar('N')


class AbstractStack(Generic[N], ABC):
    @abstractmethod
    def push(self, value: N) -> None:
        ...

    @abstractmethod
    def pop(self) -> N:
        ...

    @abstractmethod
    def __str__(self):
        pass


class Cell(Generic[T]):
    def __init__(self, value: Optional[T] = None, next: Optional['Cell'] = None):
        self.value: T = value
        self.next: Optional[Cell] = next

    def __del__(self):
        self.value = None
        self.next = None

    def __str__(self):
        return str(self.value)


class Stack(AbstractStack):
    def __init__(self):
        self.sentinel: Cell = Cell()

    def pop(self) -> Cell:
        cur_sentinel: Cell = self.sentinel
        if cur_sentinel.next is None:
            return cur_sentinel
        while cur_sentinel.next.next is not None:
            cur_sentinel: Cell = cur_sentinel.next
        cell_for_del: Cell = cur_sentinel.next
        cur_sentinel.next = None
        return cell_for_del

    def push(self, value: T) -> None:
        cur_sentinel: Cell = self.sentinel
        while cur_sentinel.next is not None:
            cur_sentinel: Cell = cur_sentinel.next
        cur_sentinel.next = Cell(value=value)

    def __str__(self):
        cur: Cell = self.sentinel
        string: str = '['
        while cur.next is not None:
            cur: Cell = cur.next
            string += str(cur) + ', '
        if string.find(', ') != -1:
            string = string[:-2]
        string += ']'
        return string


class EffectiveStack(AbstractStack):
    def __init__(self):
        self.sentinel: Cell = Cell()

    def push(self, value: T) -> None:
        pointer: Cell = self.sentinel
        new_cell: Cell = Cell(value=value)
        new_cell.next = pointer.next
        pointer.next = new_cell

    def pop(self) -> Cell:
        if self.sentinel.next is None:
            raise ValueError("Haven't some elements")
        else:
            deleted_cell = self.sentinel.next
            self.sentinel.next = self.sentinel.next.next
        return deleted_cell

    def __str__(self) -> str:
        string: str = "["
        pointer: Cell = self.sentinel
        while pointer.next is not None:
            pointer = pointer.next
            string += str(pointer) + ', '
        string += ']'
        return string


class ArrayStack(Generic[T], AbstractStack):
    def __init__(self, count=5):
        self.count = count
        self._array: List[Optional[Cell]] = [None for _ in range(self.count)]
        self.next_index = 0

    def push(self, value: T) -> None:
        self._array[self.next_index] = value
        self.next_index += 1
        if self.next_index == self.count:
            self.extend_stack()

    def extend_stack(self):
        self._array.extend([None for _ in range(self.count)])
        self.count *= 2

    def pop(self) -> T:
        if self.next_index == 0:
            raise IndexError("You ranged out")
        else:
            deleted_value = self._array[self.next_index - 1]
            self._array[self.next_index - 1] = None
            self.next_index -= 1
            return deleted_value

    def __str__(self):
        return str(self._array)


if __name__ == '__main__':
    new_stack = ArrayStack()
    for i in range(5):
        new_stack.push(i)
    print(new_stack)
    new_stack.pop()
    print(new_stack)
