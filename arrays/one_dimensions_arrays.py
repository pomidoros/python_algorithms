from typing import List, Optional, TypeVar

T = TypeVar('T')


def insert_item(arr: List, item: T, pos: Optional[int] = None) -> Optional[int]:
    if pos is None:
        arr += [item]
        return None

    length = len(arr)
    arr += [None]
    for i in range(length, pos, -1):
        arr[i] = arr[i-1]
    arr[pos] = item
    print(arr)

    return None


def delete_item(arr: List, pos: Optional[int] = None) -> Optional[T]:
    if pos is None:
        elem = arr[-1]
    else:
        for i in range(pos + 1, len(arr)):
            arr[i-1] = arr[i]
            elem = arr[pos]
    del arr[-1]
    print(arr)
    return elem


if __name__ == "__main__":
    new_array = [1, 2, 3, 4, 5]
    insert_item(new_array, 6, 3)
    delete_item(new_array, 3)
