from typing import List, Optional
from math import sqrt


def dispersion(arr: List) -> float:
    total_sum: int = 0
    mean_value: float = mean(arr)
    array_length: int = len(arr)
    for i in range(0, array_length):
        total_sum += (arr[i] - mean_value) ** 2

    return total_sum / (array_length - 1)


def mean(arr: List) -> float:
    count: int = 0
    arr_length: int = len(arr)
    for i in range(0, arr_length):
        count += arr[i]

    return float(count / arr_length)


def standard_deviation(disp: float) -> float:
    return sqrt(disp)


def median_for_sorted(arr):
    len_of_array: int = len(arr)
    if len_of_array % 2 == 0:
        return (arr[len_of_array // 2 - 1] + arr[len_of_array // 2]) / 2
    else:
        return arr[len_of_array // 2]


if __name__ == "__main__":
    new_array: List = [1, 2, 3, 4, 5]
    disp = dispersion(new_array)
    std = standard_deviation(disp)
    print(round(disp, 3))
    print(round(std, 3))
    sorted_array = [1, 2]
    print(median_for_sorted(sorted_array))
    