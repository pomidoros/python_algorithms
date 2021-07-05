from random import randint


class ArrayStack(object):
    def __init__(self, count):
        # count of the elements
        self.car_count = count
        # our array
        self.array = [None for i in range(self.car_count)]
        # for random numbers of the train's cars
        self.__u_limit = None
        self.__b_limit = None
        # for control of the array
        self.next_index = 0

    def push(self, item):
        # if cell for adding element is exceeding the highest elem
        if self.next_index == self.car_count:
            # expanding array
            self.array.extend([None for i in range(self.next_index)])
            self.car_count = self.car_count * 2
        # save item and increasing the counter
        self.array[self.next_index] = item
        self.next_index += 1

    def pop(self):
        if self.next_index == 0:
            raise ValueError("None")
        # saving value for return
        returned_value = self.array[self.next_index - 1]
        self.array[self.next_index - 1] = None
        self.next_index -= 1
        return returned_value

    # generate random train
    def generate_cars(self, b_limit, u_limit):
        self.next_index = 0
        for i in range(self.car_count):
            elem = randint(b_limit, u_limit)
            train.push(elem)

        self.__u_limit = u_limit
        self.__b_limit = b_limit

    def sort_array(self):
        array_of_stack = []
        # make stack for every type of the train's car
        for i in range(self.__u_limit - self.__b_limit + 1):
            obj = ArrayStack(self.car_count // 2)
            # and enroll it for according index in one array
            array_of_stack.append(obj)
        # go across 'train' and push items to the according stack
        while self.next_index != 0:
            cur_item = self.pop()
            # find index for the item
            index = self.__convert_item_to_index(cur_item)
            array_of_stack[index].push(cur_item)

        # go across the stacks from low to upper in the ascending order
        for i in range(self.__u_limit - self.__b_limit + 1):
            # take stack
            cur_substack = array_of_stack[i]
            while cur_substack.next_index != 0:
                # take item and psh it to the stack
                item = cur_substack.pop()
                self.push(item)

    def __convert_item_to_index(self, item):
        index = item - self.__b_limit
        return index

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return repr(self.array)


if __name__ == "__main__":
    test = False
    if test is False:
        c  = 10
    else:
        c = int(input("Input count of the train's cars: "))
    train = ArrayStack(c)
    train.push(1)
    train.push(2)
    train.push(5)
    train.generate_cars(1, 10)
    print(train)
    train.sort_array()
    print(train)