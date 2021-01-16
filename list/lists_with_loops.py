from random import randint
from list.list_methods import Node, List
from typing import Optional


class LengthException(Exception):
    pass


class MarkException(Exception):
    pass


# Inherited List for Circle algorithms
class CList(List):
    def __init__(self):
        super().__init__()
        self.pointer: Node = Node(None)

    def rand_circle(self, count: int = 10, marks: int = 0):
        # throw out Exception if length of list too few
        try:
            if count < 4:
                raise LengthException("Too few elements of circled list")
        except LengthException as exc:
            print(exc)
        # if all good
        else:
            top: Node = self.pointer
            # choose number of list on which we will be referer on loop
            loop_num: int = randint(1, count)

            loop_node = None
            # create list
            for i in range(1, count + 1):

                # generate random value
                new_value: int = randint(0, 100)

                # create Node
                top.next = Node(new_value)

                # proceed to it
                top = top.next

                # if we want to user marking algorithm, we transfer 1 to mark param
                if marks == 1:
                    # set mark to current Node
                    top.visited = False

                # save selected node
                if loop_num == i:
                    loop_node = top
                # refer last node to the selected node
                top.next = loop_node

    # check for loop by marking
    def has_loop_marking(self):
        try:
            if hasattr(self.pointer.next, "visited") is False:
                raise MarkException("Create loop by marks=1 if you want to use marking algorithm")

        except MarkException as exc:
            print(exc)

        else:
            # all nodes have been marked by False
            has_loop = False

            top = self.pointer
            while top.next is not None:

                # if next node if visited we interrupt loop
                if top.next.visited is True:
                    has_loop = True
                    top.next = None
                    break
                top = top.next

                # mark current node be True
                top.visited = True

            # take off all marks
            top = self.pointer

            while top.next is not None:
                top = top.next
                top.visited = False

            return has_loop

    def has_loop_reverse(self):
        sentinel = self.pointer
        # if list hasn't nodes - he hasn't loops
        if sentinel.next is None:
            return False
        # find the top sentinel of reversed list
        new_sentinel = self.reverse()

        # restore links after reversing
        self.reverse()

        # if the sentinel of reversed list equal to the sentinel of original list - this list has a loop
        if new_sentinel == sentinel:
            return True
        else:
            return False

    def has_loop_retracing(self):
        sentinel = self.pointer

        # go around all pointers
        while sentinel.next is not None:
            sentinel = sentinel.next

            # launch tracing detour from top sentinel
            tracing_sentinel = self.pointer

            while tracing_sentinel != sentinel:
                # if to nodes refer to single node  - this list has a loop
                if tracing_sentinel.next == sentinel.next:
                    # interrupt loop
                    sentinel.next = None
                    return True

                tracing_sentinel = tracing_sentinel.next

        return False

    def floid_algorithm(self):
        # firstly we have two pointers on the top sentinel
        rabbit = self.pointer
        turtle = self.pointer
        # launch rabbit with step 2 and launch turtle with step 1
        while rabbit.next is not None and rabbit.next.next is not None:
            rabbit = rabbit.next.next
            turtle = turtle.next
            # if turtle catch up rabbit when we have loop
            if rabbit == turtle:
                # reset to the top sentinel rabbit and launch him with step 1
                rabbit = self.pointer
                while rabbit != turtle:
                    rabbit = rabbit.next
                    turtle = turtle.next
                # when rabbit catch up turtle - stop turtle
                while rabbit.next != turtle:
                    rabbit = rabbit.next
                # interrupt the loop
                rabbit.next = None
                return True
        return False
