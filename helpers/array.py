from helpers.helpers import *
from random import randint, random


class DecoratorException(Exception):
    def __init__(self, msg=""):
        super().__init__(msg)
        self.message = msg

    def _warning_sting(self):
        return Fore.YELLOW + str(self.message) + Style.RESET_ALL

    def __str__(self):
        return str(self._warning_sting())

    def __repr__(self):
        return repr(self._warning_sting())


class NoneSortedException(DecoratorException):
    def __init__(self, msg="The array doesn't sorted"):
        super().__init__(msg)


class ArrayException(DecoratorException):
    def __init__(self, msg="Doesn't correct array"):
        super().__init__(msg)


class ArrayLimitsException(ArrayException):
    def __init__(self, msg=""):
        super().__init__(msg)


class ArrayUnicodeException(ArrayException):
    def __init__(self, msg=""):
        super().__init__(msg)


class Array(object):
    can_types = [
        type(1),
        type(""),
        type(True),
        type([1, 3, 5])
    ]

    cur_type = None

    cur_array = []

    @classmethod
    def _check_type(cls, *args):
        try:
            for arg in args:
                if type(arg) in cls.can_types:
                    if isinstance(arg, list):
                        if cls._check_type(*arg) is False:
                            return False
                    elif (cls.cur_type is None) or (cls.cur_type == arg.__class__):
                        if cls.cur_type is None:
                            cls.cur_type = type(arg)
                        cls.cur_array.append(arg)
                    else:
                        raise ArrayException
                else:
                    raise ArrayException
            return True
        except ArrayException as exc:
            print(exc)
            return False

    @classmethod
    def __clear(cls):
        cls.cur_array = []
        cls.cur_type = None
        del cls.cur_array
        del cls.cur_type

    def __new__(cls, *args):
        if cls._check_type(*args) is False:
            return None
        return super().__new__(cls)

    def __init__(self, *args, **kwargs):
        self.array = type(self).cur_array
        self.type = type(self).cur_type
        type(self).__clear()

    def __str__(self):
        return str(self.array)

    def __len__(self):
        return len(self.array)

    def __getitem__(self, item):
        return self.array[item]

    def __setitem__(self, key, value):
        self.array[key] = value

    def __iter__(self):
        return iter(self.array)

    def __next__(self):
        return next(self.array)

    def push(self, item) -> None:
        try:
            if type(item) != self.type:
                raise ArrayException("Doesn't correct type of value")
            self.array.append(item)
        except ArrayException as exc:
            print(exc)

    def pop(self):
        return self.array.pop()

    def sort(self):
        self.array.sort()


class SArray(Array):
    @property
    def is_sorted(self: List):
        i = 1
        while i < len(self):
            if self[i] < self[i - 1]:
                return False
            i += 1
        return True


class AdvancedArray(SArray):
    @staticmethod
    def __validate_methods(t: str, count: int, mini: int, maxi: int):
        available_types = [
            'int',
            'float',
            'str'
        ]
        if t not in available_types:
            return False

        if count is None or count < 0 or not isinstance(count, int):
            return False

        if not isinstance(mini, int) or not isinstance(maxi, int) or mini > maxi or mini < 0:
            return False
        return True

    @classmethod
    def random_array(cls, t: str, count: int, mini: int, maxi: int, w_range=('a', 'z'), round_num: int = 0):
        try:
            if not cls.__validate_methods(t, count, mini, maxi):
                raise ArrayException("Don't correct params")
            if t == "int" or t == "float":
                return cls.__random_numbers(t=t, count=count, mini=mini, maxi=maxi, round_num=round_num)
            elif t == "str":
                return cls.__random_words(count=count, mini=mini, maxi=maxi, w_range=w_range)
            else:
                raise ArrayException("Doesn't correct type")
        except ArrayException as exc:
            print(exc)
            return None

    @classmethod
    def __random_words(cls, count: int, mini: int, maxi: int, w_range: Tuple[str, str]):
        uni_start = ord(w_range[0])
        uni_end = ord(w_range[1])
        try:
            if uni_end < uni_start:
                raise ArrayLimitsException()
            result_list = [''.join([chr(randint(uni_start, uni_end)) for __ in range(randint(mini, maxi))]) for _ in
                           range(count)]
            return cls(result_list)
        except (ArrayLimitsException, ArrayUnicodeException) as exc:
            print(exc)
            return None

    @classmethod
    def __random_numbers(cls, t: str, count: int, mini: int, maxi: int, round_num: int = 2):
        try:
            if t == "int":
                result_list = [randint(mini, maxi) for _ in range(count)]
                return cls(result_list)
            if t == "float":
                if round_num < 0:
                    raise ArrayException("Doesn't correct round_num param")
                result_list = [round(random() * (maxi - mini) + mini, round_num) for _ in range(count)]
                return cls(result_list)
        except ArrayException as exc:
            print(exc)
            return None

    def random_index_insert(self, value):
        try:
            if isinstance(value, self.type):
                index = randint(0, len(self) - 1)
                self.array[index] = value
            else:
                raise ArrayException("Doesn't correct insert value")
        except ArrayException as exc:
            print(exc)


if __name__ == '__main__':
    obj = AdvancedArray(1, 4, 3, [1, 4, 3])
    print(obj)
    obj.random_index_insert('efw')
    print(obj)
    # RandomAdvancedArray.random_array(t="string")
    # random_array = AdvancedArray.random_array(t="float", count=10, mini=1, maxi=112, round_num=2)
    # print(random_array)
