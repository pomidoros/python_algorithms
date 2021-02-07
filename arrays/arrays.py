import numpy as np
from colorama import Fore, Style


# создаём исключение для насследования
class MyErrors(Exception):
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return repr(self.data)


# если нечётное количество аргументов - выкидываем это
class OddCountOfElemsException(MyErrors):
    pass


# если верхняя граница для определённой размерности ниже нижней - выкидываем это
class UpSmallerLowException(MyErrors):
    pass


# если слишком маленькое количество аргументов - выкидываем это
class SoLowCountException(MyErrors):
    pass


# обрабочик функций на ошибки
def handle_error(func):
    def wrapper(array, *args):
        try:
            func(array, *args)
        except MyErrors as err:
            print( Fore.YELLOW + "Occurred exception:", err.data, Style.RESET_ALL, sep=" ", end="\n")
    return wrapper


# вызываем функцию для проверки количества аргуметнов
@handle_error
def handle_len(arr, length):
    if length % 2 == 1:
        arr.pop()
        raise OddCountOfElemsException("Number of elements should be even. We trimmed it.")


# вызываем функцию для проверки правильности границ
@handle_error
def handle_up_bottom(arr, length):
    # считаем кол-во неверностей
    upper_count = 0
    for i in range(1, length, 2):
        # если неправильный порядок элементов - меняем их
        if arr[i] < arr[i - 1]:
            upper_count += 1
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
    # если есть неправильности - уведомляем о них
    if upper_count > 0:
        raise UpSmallerLowException("Some upper limit has lowed then lower limit. We change that.")


class AdvancedArray(object):
    def __init__(self, *args):
        # преобразуем кортеж в список
        list_of_args = list(args)
        # находим длину кортежа для обработки ошибок
        len_of_args = len(args)

        # начинается блок обработки ошибок
        if len_of_args < 2:
            raise SoLowCountException("Too little count of the arguments")
        handle_len(list_of_args, len_of_args)
        handle_up_bottom(list_of_args, len_of_args)
        # заканчивается блок обработки ошибок

        # пакуем преобразованный список обратно в кортеж
        args = tuple(list_of_args)

        # размерность массива
        self.dim = len(args) // 2
        # получаем верхние  нижние границы
        self.lower_limits = [args[i] for i in range(len(args)) if i % 2 == 0]
        self.upper_limits = [args[i] for i in range(len(args)) if i % 2 == 1]

        # создаём массив
        self.__array = self.make_array()

        # счётчики для обращения к объекту как к массиву
        self.cur_treat = []
        self.counter = 0

    def __getitem__(self, key):
        # при каждом обращении к объекту как к элементу массива - заполняем этот список правильными значениями
        self.cur_treat.append(self.handled_key(key))
        # если добавлены все нужные ячейки
        if self.counter == self.dim - 1:
            # находим нужную ячейку
            result = self.find_cell()
            # обнуляем ненужное
            self.counter = 0
            self.cur_treat = []
            # возввращаем ячейку
            return result
        else:
            # иначе увеличиваем счётчик  возвращаем объект
            self.counter += 1
            return self

    def __setitem__(self, key, value):
        # добавляем последнюю ячейку
        self.cur_treat.append(self.handled_key(key))
        # копируем ссылку на массив
        cell = self.__array
        # получаем n-1 нужную размерность
        for i in range(len(self.cur_treat) - 1):
            cell = cell[self.cur_treat[i]]
        # в последнюю ячейку вставляем новое значение
        cell[self.cur_treat[-1]] = value
        # обнуляем всё
        self.counter = 0
        self.cur_treat = []

    # находим корректное значение
    def handled_key(self, it):
        return it - self.lower_limits[self.counter]

    # находим нужную ячейку с уже готовым списком
    def find_cell(self):
        cell = self.__array
        for i in range(len(self.cur_treat)):
            cell = cell[self.cur_treat[i]]
        return cell

    # заполняем массив нужной размерности нулями
    def make_array(self):
        dims = 1
        list_of_dims = []
        # находим кол-во элементов и заполняем размерности для каждого уровня
        for (i, j) in zip(self.lower_limits, self.upper_limits):
            dims *= (j - i + 1)
            list_of_dims.append(j - i + 1)
        # строим одномерный массив из нулей
        arr = np.zeros((dims,), dtype="int")
        # преобразуем его в нужную форму
        arr = arr.reshape(*list_of_dims).tolist()
        return arr

    def __str__(self):
        return str(self.__array)


if __name__ == "__main__":
    obj = AdvancedArray(1000, 1002, 504, 505, 42, 46, 12)
    obj[1001][505][42] = 10
    print(obj)
    print(obj[1001][505][42])


