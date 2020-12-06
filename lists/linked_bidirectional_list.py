
class Cell:
    def __init__(self, val, prev=None, next=None):
        self.value = val
        self.prev = prev
        self.next = next


class BiList:
    def __init__(self):
        self.pointer_first = Cell(None)
        self.pointer_last = Cell(None)
        self.pointer_first.next = self.pointer_last
        self.pointer_last.prev = self.pointer_first

    def add_head(self, val):
        top = self.pointer_last.prev
        new = Cell(val)
        new.next = top.next
        top.next = new
        new.prev = top
        new.next.prev = new

    def __str__(self):
        string = '['
        top = self.pointer_first
        while top.next.next is not None:
            top = top.next
            string += str(top.value) + ', '
        return string[:-2] + ']'
