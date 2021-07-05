from helpers.helpers import *
from functools import reduce


class Exponentiation(object):
    @staticmethod
    def raise_to_power(a: float, p: int):
        if p == 0:
            return 1
        bin_power = bin(p)[2:][::-1]
        all_powers = [a ** (2 ** i) for i, val in enumerate(bin_power) if int(val) == 1]
        result = reduce(lambda x, y: x * y, all_powers)
        return result

    @staticmethod
    def minimum_degree_upper_number(number: int, degree_of: int = 2) -> int:
        i, cur_degree = 0, 1
        while cur_degree < number:
            i += 1
            cur_degree = Exponentiation.raise_to_power(degree_of, i)
        return cur_degree


if __name__ == '__main__':
    Exponentiation.raise_to_power(7, 0)
