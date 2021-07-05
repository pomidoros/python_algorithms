from random import randrange, random


class RandomArray(object):

    types = {
        1: "int",
        2: "float",
        3: "string"
    }

    def __init__(self, count: int, typeof: int = 1, minimum: int = 0, maximum: int = 10, accuracy: int = None):
        self.count = count
        self.typeof = typeof
        self.minimum = minimum
        self.maximum = maximum
        if RandomArray.types[typeof] == "float":
            self.accuracy = accuracy
        else:
            self.accuracy = None
        self.array = self.define_type()

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return repr(self.array)

    def define_type(self):
        name_of_method = "_generate_random_" + RandomArray.types[self.typeof]
        if name_of_method in RandomArray.__dict__:
            return RandomArray.__dict__[name_of_method](self)

    def _generate_random_string(self):
        array_string = list()
        for i in range(self.count):
            random_length = randrange(self.minimum, self.maximum + 1)
            string = []
            for j in range(random_length):
                string.append(chr(randrange(97, 123)))
            array_string.append("".join(string))
        return array_string

    def _generate_random_int(self):
        output_array = []
        for i in range(self.count):
            output_array.append(randrange(self.minimum, self.maximum + 1))
        return output_array

    def _generate_random_float(self):
        output_array = []
        for i in range(self.count):
            random_float = random() * (self.maximum - self.minimum) + self.minimum
            output_array.append(round(random_float, self.accuracy))
        return output_array

    def get_array(self):
        return self.array


if __name__ == '__main__':
    test = RandomArray(10, 2, accuracy=2)
    print(test)
