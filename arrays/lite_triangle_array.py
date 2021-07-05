class LiteLeftTriangleArray(object):
    def __init__(self, arg):
        self._dim = arg ** 2 // 2
        self._array = [0] * self._dim

    def __convert_cell(self, arg1, arg2):
        if arg1 < arg2:
            return self.__convert_cell(arg2, arg1)
        else:
            return arg1 * (arg1 + 1) // 2 + arg2

    def set(self, *args):
        if len(args) != 3:
            raise ValueError
        else:
            index = self.__convert_cell(args[0], args[1])
            self._array[index] = args[2]

    def get(self, *args):
        if len(args) != 2:
            raise ValueError
        else:
            index = self.__convert_cell(args[0], args[1])
            return self._array[index]


class LiteRightTriangleArray(LiteLeftTriangleArray):
    def __init__(self, arg):
        super().__init__(arg)

    def __convert_cell(self, arg1, arg2):
        if arg2 < arg1:
            return self.__convert_cell(arg2, arg1)
        else:
            return arg2 * (arg2 + 1) // 2 + arg1


if __name__ == "__main__":
    new_left_array = LiteLeftTriangleArray(10)
    new_left_array.set(2, 3, 10)
    print(new_left_array.get(2, 3))

    new_right_array = LiteRightTriangleArray(10)
    new_right_array.set(9, 2, 10)
    print(new_right_array.get(2, 9))
    print(new_right_array.get(9, 2))
