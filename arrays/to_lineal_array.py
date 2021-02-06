class LikeLineal(object):
    def __init__(self, *dims):
        # количество размерностей
        self.num_dimensions = len(dims)
        # границы размерностей
        self.bounds = dims
        # слои для каждой размерности
        self.slice_sizes = []
        # создание нужного массива
        self.__array = self.make_lineal_array()
        # для корректной работы
        self.cur_elem = 0
        self.counter = 0

    def make_lineal_array(self):
        slice_size = 1
        # проходим с конца по размерностям
        for i in range(self.num_dimensions - 1, -1, -1):
            # добавляем для каждой размерности размер слоя, который он содержит
            self.slice_sizes.insert(0, slice_size)
            # считаем общий размер послойно
            slice_size *= self.bounds[i]
        return [0] * slice_size

    def __str__(self):
        return str(self.__array)

    def __getitem__(self, item):
        # если дошли до конца - просто прибавляем последний индекс
        if self.counter == self.num_dimensions - 1:
            self.cur_elem += item

            # аннулируепм элементы поиска
            self.counter = 0
            self.cur_elem = 0

            return self.cur_elem
        # если не дошли до конца
        else:
            # прибавляем содержащееся число слоёв
            self.cur_elem += item * self.slice_sizes[self.counter]
            # увеличиваем счётчк на один
            self.counter += 1
            # возвращаем сам элемент
            return self

    def print_length(self):
        print(len(self.__array))


if __name__ == "__main__":
    new_array = LikeLineal(2, 3, 4)
    print(new_array[1][1][1])


