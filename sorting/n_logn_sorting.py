from helpers.helpers import *
from math import ceil

T = TypeVar('T')


class Heap(Generic[T]):
    def __init__(self, values: List[T]):
        self._values: List[T] = values
        self._heap: List[Optional[T]] = []
        self._length = 0
        self._make_heap()

    def _make_heap(self) -> None:
        for value in self._values:
            self.add(value)

    def add(self, item: T) -> None:
        self._heap.append(item)
        self._length += 1
        cur_index = self._length - 1
        while True:
            parent_index = (cur_index - 1) // 2
            if parent_index < 0:
                return
            if self._heap[cur_index] > self._heap[parent_index]:
                self._heap[cur_index], self._heap[parent_index] = self._heap[parent_index], self._heap[cur_index]
            else:
                return
            cur_index = parent_index

    def remove(self) -> T:
        output = self._heap[0]
        self._heap[-1], self._heap[0] = self._heap[0], self._heap[-1]
        self._heap.pop()
        self._length -= 1
        if len(self) == 0:
            return output
        cur_index = 0
        while True:
            child1 = cur_index * 2 + 1
            child2 = cur_index * 2 + 2
            if child1 >= len(self):
                child1 = cur_index
            if child2 >= len(self):
                child2 = cur_index
            swap_index = child1 if self._heap[child1] >= self._heap[child2] else child2
            if self._heap[cur_index] >= self._heap[swap_index]:
                return output
            self._heap[cur_index], self._heap[swap_index] = self._heap[swap_index], self._heap[cur_index]
            cur_index = swap_index

    def __str__(self) -> str:
        return str(self._heap)

    def __len__(self) -> int:
        return self._length


def heap_sorting(arr: List[T]):
    new_array = []
    heap = Heap(arr)
    for i in range(len(heap)):
        new_array.append(heap.remove())
    return new_array


if __name__ == '__main__':
    array = [4, 3, 7, 34, 1, 643, 8, 2]
    print(heap_sorting(array))
    heap = Heap(array)
