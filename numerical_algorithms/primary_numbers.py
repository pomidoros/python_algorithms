from helpers.helpers import *
from random import randint
from math import sqrt, ceil
from numerical_algorithms.exponentiation import Exponentiation


class PrimaryNumbers:
    @staticmethod
    def is_primary_by_fermat(number: int, tests: int = 5) -> bool:
        closed_tests = []
        for i in range(tests):
            random_test = randint(1, number - 1)
            while random_test in closed_tests:
                random_test = randint(1, number - 1)
            closed_tests.append(random_test)
            if Exponentiation.raise_to_power(random_test, number - 1) % number != 1:
                return False
        return True

    @staticmethod
    def is_primary_by_check(number: int) -> bool:
        for divider in range(2, ceil(sqrt(number))):
            if number % divider == 0:
                return False
        return True

    @staticmethod
    def find_factors(number: int) -> Optional[List[int]]:
        all_factors = []
        while number % 2 == 0:
            all_factors.append(2)
            number //= 2
        divider = 3
        max_factor = sqrt(number)
        while divider <= max_factor:
            while number % divider == 0:
                all_factors.append(divider)
                number //= divider
            max_factor = sqrt(number)
            divider += 2
        if number > 1:
            all_factors.append(number)
        return all_factors

    @staticmethod
    def find_primes(limiter: int) -> List[int]:
        is_composites = [False] * (limiter + 1)
        for i in range(4, limiter + 1, 2):
            is_composites[i] = True
        cur_ind = 3
        while cur_ind <= sqrt(limiter):
            for i in range(2 * cur_ind, limiter + 1, cur_ind):
                is_composites[i] = True
            cur_ind += 2
            while is_composites[cur_ind] is True:
                cur_ind += 2
        return [i for i, val in enumerate(is_composites) if i > 1 and val is False]

    @staticmethod
    def minimum_prime_upper_number(low_limiter: int) -> int:
        iteration = low_limiter
        while PrimaryNumbers.is_primary_by_fermat(iteration) is False:
            iteration += 1
        return iteration


if __name__ == '__main__':
    PrimaryNumbers.is_primary_by_fermat(13)
