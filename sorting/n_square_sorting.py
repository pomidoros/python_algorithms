from helpers import random_array as ra
from helpers.helpers import *

T = TypeVar("T")


def insert_sorting(arr: List[T]) -> List[T]:
    output_array = [arr.pop()]
    while len(arr) != 0:
        cur_item = arr.pop()
        id = 0
        while cur_item >= output_array[id] and (id < len(output_array) - 1):
            id += 1
        output_array.insert(id, cur_item)
    return output_array


def insert_sorting_in_place(arr: List[T]):
    for i in range(1, len(arr)):
        cur_item = arr.pop(i)
        j = 0
        while (j < i) and (cur_item >= arr[j]):
            j += 1
        arr.insert(j, cur_item)


def select_sorting(arr: List[T]):
    output_array = []
    for i in range(len(arr)):
        min_id = 0
        for j in range(1, len(arr)):
            if arr[j] < arr[min_id]:
                min_id = j
        output_array.append(arr[min_id])
        arr.pop(min_id)
    return output_array


def select_sorting_in_place(arr: List[T]):
    output_array = []
    for i in range(len(arr)):
        min_id = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_id]:
                min_id = j
        arr[0], arr[min_id] = arr[min_id], arr[0]


def bubble_sorting(arr: List[T]):
    for i in range(len(arr)):
        max_id = 0
        for j in range(len(arr) - i):
            if arr[max_id] >= arr[j]:
                arr[max_id], arr[j] = arr[j], arr[max_id]
            max_id = j


if __name__ == '__main__':
    array = ra.RandomArray(10, 1, 10, 100).get_array()
    print(array)
    bubble_sorting(array)
    print(array)
