class DoubleStackArray(object):
    def __init__(self, n=20):
        self.num = n
        self.array = [None for i in range(self.num)]
        self.next_left = 0
        self.next_right = self.num - 1

    def push_l(self, item):
        if self.next_left > self.next_right:
            raise ValueError("We can't push it")
        self.array[self.next_left] = item
        self.next_left += 1

    def push_r(self, item):
        if self.next_left > self.next_right:
            raise ValueError("We can't push it")
        self.array[self.next_right] = item
        self.next_right -= 1

    def pop_l(self):
        if self.next_left == 0:
            raise ValueError("You can't realize it")
        self.next_left -= 1
        output_value = self.array[self.next_left]
        self.array[self.next_left] = None
        return output_value

    def pop_r(self):
        if self.next_right == self.num - 1:
            raise ValueError("You can't realize it")
        self.next_right += 1
        output_value = self.array[self.next_right]
        self.array[self.next_right] = None
        return output_value

    def __str__(self):
        return str(self.array)

    def __repr__(self):
        return repr(self.array)



if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()

    ar_stack = StackArray()
    ar_stack.push(1)
    ar_stack.push(2)
    ar_stack.push(3)
    ar_stack.pop()

    d_stack = DoubleStackArray()
    d_stack.push_l(3)
    d_stack.push_l(2)
    d_stack.push_r(4)
    d_stack.push_r(5)