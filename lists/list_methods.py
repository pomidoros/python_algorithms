import random as rd


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.ind)


class List:
    def __init__(self):
        self.pointer = Node(None)

    def add_node(self, value):
        top = self.pointer
        while top.next is not None:
            top = top.next
        new_node = Node(value)
        top.next = new_node

    def add_nodes(self, *values):
        for val in values:
            self.add_node(val)

    def add_to_head(self, value):
        top = self.pointer
        new_cell = Node(value)
        new.next = top.next
        top.next = new_cell

    def find_node(self, value):
        top = self.pointer
        inc = 0
        while top.next is not None:
            top = top.next
            inc += 1
            if top.value == value:
                return inc
        return None

    def insert_node(self, after_me, value):
        top = self.pointer
        inc = 0
        while top.next is not None:
            top = top.next
            inc += 1
            if inc == after_me:
                new = Node(value)
                new.next = top.next
                top.next = new

    def delete_node(self, index):
        top = self.pointer
        for i in range(index):
            top = top.next
        top.next.next, top.next = None, top.next.next

    def copy_list(self):
        new_sentinel = List()
        top = self.pointer.next
        while top is not None:
            new_sentinel.add_node(top.value)
            top = top.next
        return new_sentinel

    def __str__(self):
        string = 'Start << ['
        top = self.pointer
        while top.next.next is not None:
            top = top.next
            string += str(top.value) + ', '
        string += str(top.next.value) + '] << End'
        return string

    def generator_print(self):
        top = self.pointer
        while top.next is not None:
            top = top.next
            yield top.value

    def random_list(self):
        sentinel = self.pointer
        n = rd.randint(1, 10)
        for i in range(n):
            elem = rd.randint(1, 30)
            sentinel.next = Node(elem)
            sentinel = sentinel.next




if __name__ == "main":
    new = List()
    new.addNodes(*[1, 2, 3, 5])
