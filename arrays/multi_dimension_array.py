from abc import ABC, abstractmethod


class MultiArray(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @abstractmethod
    def find_index(self, *args):
        pass

    @abstractmethod
    def set_cell(self, *args, val=None):
        pass

    @abstractmethod
    def get_cell(self, *args):
        pass


class UsualMultiDimension(MultiArray):
    def __init__(self, *args):
        self.dims = args
        self.count_of_array = len(args)
        self.bounds = [0] * self.count_of_array
        self.array = [0] * UsualMultiDimension.len_of_array(*args)
        self.make_bounds()

    @staticmethod
    def len_of_array(*dims):
        result = 1
        for dim in dims:
            result *= dim
        return result

    def make_bounds(self):
        bound = 1
        for i in range(self.count_of_array - 1, -1, -1):
            self.bounds[i] = bound
            bound *= self.dims[i]

    def get_cell(self, *args):
        index = self.find_index(*args)
        return self.array[index]

    def find_index(self, *indices):
        index = 0
        for ind in range(len(indices)):
            index += self.bounds[ind] * indices[ind]
        return index

    def set_cell(self, *args, val=None):
        index = self.find_index(*args)
        self.array[index] = val


class AdvancedMultiDimension(MultiArray):
    def __init__(self, *args):
        # count of the arguments
        self.length_of_args = len(args)
        # count of the dimensions
        self.count_of_dims = self.length_of_args // 2

        # fill in the lower and upper bounds
        self.lower_bounds = []
        self.upper_bounds = []
        self.make_up_down_bounds(*args)

        self.array = self.count_of_elements() * [0]
        self.bounds = [0] * self.count_of_dims
        self.fill_bounds()

    def make_up_down_bounds(self, *args):
        for i in range(self.length_of_args):
            if i % 2 == 0:
                self.lower_bounds.append(args[i])
            else:
                self.upper_bounds.append(args[i])

    def fill_bounds(self):
        current_bound = 1
        for i in range(self.count_of_dims - 1, -1, -1):
            self.bounds[i] = current_bound
            current_bound *= self.upper_bounds[i] - self.lower_bounds[i]

    def count_of_elements(self):
        layout = 1
        for i in range(self.count_of_dims):
            layout *= self.upper_bounds[i] - self.lower_bounds[i]
        return layout

    def get_cell(self, *args):
        index = self.find_index(*args)
        return self.array[index]

    def set_cell(self, *args, val=None):
        index = self.find_index(*args)
        self.array[index] = val

    def find_index(self, *elems):
        index = 0
        for i in range(len(elems)):
            index += self.bounds[i] * (elems[i] - self.lower_bounds[i])
        return index


class SuperAdvancedMultiDimension(MultiArray):
    def __init__(self, *args, inc=False):
        self.state_of_upper = int(inc)
        self.len_of_args = len(args)
        self.dims = self.len_of_args // 2
        self.lower_bounds = []
        self.upper_bounds = []
        self.fill_up_down_bounds(*args)
        self.bounds = [0] * self.dims
        self.array = [0] * self.construct_layouts()

        self.counter = 0
        self.list_of_required_cells = []

    def fill_up_down_bounds(self, *args):
        for i in range(self.len_of_args):
            if i % 2 == 0:
                self.lower_bounds.append(args[i])
            else:
                self.upper_bounds.append(args[i])

    def construct_layouts(self):
        current_layout = 1
        for i in range(self.dims - 1, -1, -1):
            self.bounds[i] = current_layout
            current_layout *= self.upper_bounds[i] - self.lower_bounds[i] + self.state_of_upper
        return current_layout

    def find_index(self, *args):
        index = 0
        for i in range(len(args)):
            index += self.bounds[i] * (args[i] - self.lower_bounds[i])
        return index

    def check_cells_for_correct(self, *cells):
        for i in range(self.dims):
            if (cells[i] < self.lower_bounds[i]) or (cells[i] >= (self.upper_bounds[i] + self.state_of_upper)):
                print(cells[i])
                print(self.lower_bounds[i])
                print(self.upper_bounds[i])
                raise Exception("Ex")
            else:
                continue

    def set_cell(self, *args, val=None):
       self.check_cells_for_correct(*args)
       index = self.find_index(*args)
       self.array[index] = val

    def get_cell(self, *args):
        self.check_cells_for_correct(*args)
        return self.array[self.find_index(*args)]

    def __getitem__(self, item):
        self.counter += 1
        self.list_of_required_cells.append(item)
        if self.counter == self.dims:
            cell = self.get_cell(*tuple(self.list_of_required_cells))
            self.counter = 0
            self.list_of_required_cells = []
            return cell
        elif self.counter > self.dims:
            raise Exception("Mdeeee")
        else:
            return self

    def __setitem__(self, key, value):
        self.counter += 1
        if self.counter != self.dims:
            raise Exception("Mdeee")
        else:
            self.list_of_required_cells.append(key)
            self.set_cell(*tuple(self.list_of_required_cells), val=value)
            self.counter = 0
            self.list_of_required_cells = []


if __name__ == "__main__":
    make_array = UsualMultiDimension(3, 4, 5)
    make_array.set_cell(1, 1, 2, val=10)

    make_advanced_array = AdvancedMultiDimension(0, 3, 0, 4, 0, 5)
    make_advanced_array.set_cell(1, 1, 2, val=10)

    super_adv_array = SuperAdvancedMultiDimension(0, 3, 0, 4, 1, 6)
    super_adv_array.set_cell(1, 1, 3, val=10)
    super_adv_array[1][3][5] = 15
    print(super_adv_array[1][3][5])

    


