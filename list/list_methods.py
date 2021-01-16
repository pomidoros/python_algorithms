import time


# class of every Node of List
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# class of List and his methods
class List:
    def __init__(self):
        self.pointer = Node(None)

    def __str__(self):
        start_time = time.time()
        string = "["
        top = self.pointer
        start_time = time.time()
        while top.next is not None:
            if time.time() - start_time > 2:
                return "Infinity loop"
            top = top.next
            string += str(top.value) + ', '
        return string[:-2] + "]"

    @property
    def length(self):
        top = self.pointer
        count = 0
        while top.next is not None:
            top = top.next
            count += 1
        return count

    def append(self, value):
        top = self.pointer
        while top.next is not None:
            top = top.next
        new_node = Node(value)
        top.next = new_node

    # extend by other object of List() class
    def extend(self, other):
        top = self.pointer
        while top.next is not None:
            top = top.next
        other_top = other.pointer.next
        top.next = other_top

    def pop(self):
        top = self.pointer
        count = 0
        while count + 1 != self.length:
            top = top.next
            count += 1
        deleted_cell = top.next.value
        top.next = top.next.next
        return deleted_cell

    def popleft(self):
        top = self.pointer
        deleted_cell = top.next
        top.next = top.next.next
        return deleted_cell

    # ATTENTION: marks don't copy
    def copy(self):
        # current sentinel
        top = self.pointer
        # miss sentinel
        last_added = top.next
        # create new list
        new_list = List()
        # take new sentinel
        new_top = new_list.pointer
        while last_added is not None:
            new_top.next = Node(last_added.value)
            last_added = last_added.next
            new_top = new_top.next
        return new_list

    def reverse(self):
        # set lower sentinel
        prev_node = None
        # get first meaningful value
        cur_node = self.pointer
        # while not reach end sentinel
        while cur_node is not None:
            # take next value
            next_node = cur_node.next
            # reverse link
            cur_node.next = prev_node

            # move current nodes
            prev_node = cur_node
            cur_node = next_node
        self.pointer = prev_node
        return prev_node
