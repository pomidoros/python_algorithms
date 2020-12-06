class Node:
    def __init__(self, value, inc=-1, next=None):
        self.value = value
        self.next = next
        self.ind = inc

    def __str__(self):
        return str(self.ind)


class List:
    def __init__(self):
        self.pointer = Node(None)

    def add_node(self, value):
        top = self.pointer
        inc = 0
        while top.next is not None:
            top = top.next
            inc += 1
        new_node = Node(value, inc)
        top.next = new_node

    def add_nodes(self, *values):
        for val in values:
            self.add_node(val)

    def add_to_head(self, value):
        top = self.pointer
        new = Node(value)
        new.next = top.next
        top.next = new
        while top.next is not None:
            top = top.next
            top.ind += 1

    def __str__(self):
        string = 'Start << ['
        top = self.pointer
        while top.next.next is not None:
            top = top.next
            string += str(top.value) + ', '
        string += str(top.next.value) + '] << End'
        return string

    def find_node(self, value):
        top = self.pointer
        while top.next is not None:
            top = top.next
            if top.value == value:
                return top.ind
        return None

    def insert_node(self, after_me, value):
        top = self.pointer
        while top.next is not None:
            top = top.next
            if top.ind == after_me:
                new = Node(value, top.ind)
                new.next = top.next
                top.next = new
                while top.next is not None:
                    top = top.next
                    top.ind += 1

    def delete_node(self, index):
        top = self.pointer
        for i in range(index):
            top = top.next
        top.next.next, top.next = None, top.next.next


if __name__ == "main":
    new = List()
    new.addNodes(*[1, 2, 3, 5])
