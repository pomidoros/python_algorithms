from helpers.helpers import *


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        pass


class List:
    def __init__(self):
        self.sentinel = Node()

    def insert(self, item):
        cur_limit = self.sentinel
        while cur_limit.next is not None:
            if cur_limit.next.value > item:
                new_node = Node(item, cur_limit.next)
                cur_limit.next = new_node
                return
            cur_limit = cur_limit.next
        cur_limit.next = Node(item)
        return

    def find(self, item):
        counter = 0
        cur_limit = self.sentinel
        while cur_limit.next is not None:
            counter += 1
            if cur_limit.next.value == item:
                return item, counter
            if cur_limit.value.value > item:
                return None
        return None


    def delete(self, item):
        pass


class Array:
    def __init__(self, length=10):
        self.length = length
        self._array = [] * length

    def add(self, item):

        """
        :param item:
        :return:
        """
        return

    def drop(self, item):
        """
        :param item:
        :return:
        """
        return

    def hash_function(self, item):
        return int(item) % self.length


if __name__ == '__main__':
    obj = Array()
    help(obj)
