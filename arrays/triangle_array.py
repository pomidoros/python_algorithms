from colorama import Fore, Style


class ToLowArrayException(Exception):
    pass


class NoneCorrectDimException(Exception):
    pass

class NoneCorrectItem(Exception):
    pass


class ArrayToLarge(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return str(self.data)


class TriangleArray(object):
    def __init__(self, *dims):
        # обрабатываем переданные аргументы
        self.dim = TriangleArray.handle_bounds(*dims)
        # заполняем массив по правилам
        self.__array = self.make_triangle_array()

        # ставим счётчики
        self.counter = 0
        self.indexes = []

    # создаём массив нужной размерности
    def make_triangle_array(self):
        return [None] * (self.dim * (self.dim + 1) // 2)

    # находим координату по заданным двум
    def find_index(self):
        return (self.indexes[0] * (self.indexes[0] + 1) // 2) + self.indexes[1]

    def __getitem__(self, item):
        # Проверяем элемент на ликвидность
        self.check_item(item)
        # увеличиваем счётчик
        self.counter += 1
        # добавляем новый элемент в список
        self.indexes.append(item)
        # если все элементы получены
        if self.counter == 2:
            index = self.end_of_getting_index()
            return self.__array[index]
        # если получены не все элементы - возвращаем объект
        else:
            return self

    def __setitem__(self, key, value):
        # Проверяем элемент на ликвидность
        self.check_item(key)
        # добавляем последний элемент
        self.indexes.append(key)
        index = self.end_of_getting_index()
        self.__array[index] = value

    # если столбец больше строки - меняем их местами
    def swipe_elems(self):
        if self.indexes[0] < self.indexes[1]:
            self.indexes[0], self.indexes[1] = self.indexes[1], self.indexes[0]

    # зануление обработчиков
    def discharge_getting(self):
        self.counter = 0
        self.indexes = []

    # возвращает индекс и зануляет обработчики
    def end_of_getting_index(self):
        # меняем индексы местами, если столбец больше строки
        self.swipe_elems()
        # сохраняем индексы
        index = self.find_index()
        # зануляем обработчики
        self.discharge_getting()
        return index

    def check_item(self, it):
        if (it > self.dim) or (it < 0):
            raise NoneCorrectDimException("Lower then 0 or More then the dimension")

    # обработка ошибок
    @staticmethod
    def handle_bounds(*limits):
        # если аргументов нет
        if len(limits) < 1:
            raise ToLowArrayException("Number of dimensions should be more then 1")

        try:
            # если аргументов больше одного
            if len(limits) > 1:
                raise ArrayToLarge("To many arguments. We have trimmed them")
        except ArrayToLarge as err:
            print(Fore.YELLOW + "Occurred exception:", err.data, Style.RESET_ALL, sep=" ", end="\n")

        if limits[0] < 1:
            raise NoneCorrectDimException("None correct value")

        return limits[0]

    def __str__(self):
        return str(self.__array)


if __name__ == "__main__":
    triangle_array = TriangleArray(12)
    triangle_array[0][3] = 10
    print(triangle_array[0][3])