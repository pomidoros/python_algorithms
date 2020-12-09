from math import ceil
#cell with 'visited' attribute
class Cellv:
    def __init__(self, value, next=None):
        self.value = value
        self.visited = False
        self.next = next


#cell without 'visited' attribute
class Cell:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def iterate(top):
    count, restriction = 0, 10
    while top.next is not None:
        top = top.next
        print(top.value)
        count += 1
        if count > restriction:
            break


def iterate_reverse(top):
    while top.next is not None:
        print(top.value)
        top = top.next


def add_to_end(top, new_cell):
    while top.next is not None:
        top = top.next
    top.next = new_cell


def find_length(top):
    i = 0
    sentinel = top
    while sentinel.next is not None:
        i += 1
        sentinel = sentinel.next
    return i


def make_circle(sentinel):
    top = sentinel
    if find_length(top) < 2:
        return "can't make the loop"
    else:
        point_number = ceil(find_length(top) / 2)
        it = 0
        while top.next is not None:
            top = top.next
            it += 1
            if it == point_number:
                point_for = top
        top.next = point_for
    return sentinel


def has_loop_marking(top: Cellv):
    has_loop = False
    sentinel = top
    while sentinel.next is not None:
        if sentinel.next.visited:
            sentinel.next = None
            has_loop = True
            break
        sentinel = sentinel.next
        sentinel.visited = True

    sentinel = top
    while sentinel.next is not None:
        sentinel = sentinel.next
        sentinel.visited = False
    return has_loop


def has_loop_retracing(top: Cell):
    has_loop = False
    sentinel = top
    while sentinel.next is not None:
        tracer = top
        while tracer != sentinel:
            if tracer.next == sentinel.next:
                has_loop = True
                sentinel.next = None
                return has_loop
            tracer = tracer.next
        sentinel = sentinel.next
    return has_loop


def reverse_list(top: Cell):
    prev_cell = None
    curr_cell = top
    while curr_cell is not None:
        next_cell = curr_cell.next
        curr_cell.next = prev_cell
        prev_cell = curr_cell
        curr_cell = next_cell
    return prev_cell


def has_loop_reversing(top: Cell):
    if top.next is None:
        return False
    new_sentinel = reverse_list(top)
    reverse_list(new_sentinel)
    if new_sentinel == top:
        return True
    else:
        return False
