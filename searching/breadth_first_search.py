from helpers.helpers import *
from stacks_and_deques.queue import Queue

T = TypeVar('T')


def breadth_first_search(start: T, func: Callable):
    queue = Queue()
    queue.push(start)
    result_list = []
    while queue != 0:
        cur_item: T = queue.pop()
        result_list.append(cur_item)
        for child in func(cur_item):
            queue.push(child)
    return result_list
