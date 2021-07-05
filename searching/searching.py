from functools import wraps
import matplotlib as plt
import time
from helpers.array import *


T = TypeVar('T')


def time_for_method(method):
    @wraps(method)
    def wrapper(*args):
        start_time = time.time()
        result = method(*args)
        end_time = time.time()
        time_diff = end_time - start_time
        print(time_diff)
        return result
    return wrapper


def time_for_class(cls):
    for attribute in dir(cls):
        if attribute.startswith("__") and attribute.endswith("__") or attribute.startswith("_abc") or attribute.startswith("_gorg"):
            continue
        cur_cls_attribute = getattr(cls, attribute)
        if hasattr(cur_cls_attribute, "__call__"):
            changed_method = time_for_method(cur_cls_attribute)
            setattr(cls, attribute, changed_method)
    return cls


@time_for_class
class Search(Generic[T]):
    @classmethod
    def linear(cls, array: SArray, value: T) -> Optional[int]:
        try:
            if not array.is_sorted:
                raise NoneSortedException()
            cur_index = -1
            for elem in array:
                cur_index += 1
                if value != elem:
                    continue
                return cur_index
            return -1
        except NoneSortedException as exc:
            print(exc)
            return None

    @classmethod
    def binary(cls, array: SArray, value: T) -> Optional[int]:
        try:
            if not array.is_sorted:
                raise NoneSortedException()
            mini = 0
            maxi = len(array) - 1
            while mini < maxi:
                middle = (maxi + mini) // 2
                if array[middle] < value:
                    mini = middle + 1
                if array[middle] > value:
                    maxi = middle - 1
                else:
                    return middle
            if array[mini] == value:
                return mini
            else:
                return -1
        except NoneSortedException as exc:
            print(exc)
            return None

    @classmethod
    def interpolation(cls, array: SArray, value: T) -> Optional[int]:
        try:
            if not array.is_sorted:
                raise NoneSortedException()
            mini = 0
            maxi = len(array) - 1
            while mini < maxi:
                relevant_item = mini + (value - array[mini]) * (maxi - mini) // (array[maxi] - array[mini])
                if value < array[relevant_item]:
                    maxi = relevant_item - 1
                elif value > array[relevant_item]:
                    mini = relevant_item + 1
                else:
                    return relevant_item
            if array[mini] == value:
                return mini
            else:
                return -1

        except NoneSortedException as exc:
            print(exc)
            return None


if __name__ == '__main__':
    obj = AdvancedArray.random_array(t='int', count=1, mini=1, maxi=1000000)
    obj[0] = 1000001
    obj.sort()
    result1 = Search.linear(obj, 1000001)
    print(result1)
    result2 = Search.binary(obj, 1000001)
    print(result2)
    result3 = Search.interpolation(obj, 1000001)
    print(result3)