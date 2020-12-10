class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None


def iterate(top: Cell):
    string = '['
    while top.next is not None:
        top = top.next
        string += str(top.value) + ', '
    string += ']'
    print(string)


def add_to_end(top: Cell, new_cell: Cell):
    while top.next is not None:
        top = top.next
    top.next = new_cell


def add_to_head(top: Cell, new: Cell):
    new.next = top.next
    top.next = new


def insert_sort(top: Cell):
    sentinel = Cell(None)
    top = top.next
    while top is not None:
        new_cell = top
        top = top.next
        after_me = sentinel
        while after_me.next is not None and after_me.next.value < new_cell.value:
            after_me = after_me.next
        new_cell.next = after_me.next
        after_me.next = new_cell
    return sentinel


def copy_list(top: Cell):
    sentinel = Cell(None)
    last_added = sentinel
    top = top.next
    while top is not None:
        last_added.next = Cell(None)
        last_added = last_added.next
        last_added.value = top.value
        top = top.next
    return sentinel


