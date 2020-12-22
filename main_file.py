# unidirectional list methods package
from lists import list_methods as lm
# bidirectional list methods package
from lists import bidirectional_list_methods as bl
# list functions
from lists import list_func as lf
# list with loop functions
from lists import lists_with_loop as ll
# list's visualization
from lists import interface_for_lists as inter


# example of onedirectional binding lists' methods
def example_list_methods():
    new_list = lm.List()
    new_list.add_nodes(*[1, 2, 3])


def example_insert_sort_of_lists():
    sentinel = lf.Cell(None)
    list_of_values = [3, 5, 7, 3, 2, 5, 10, 14, 11]
    for num in list_of_values:
        lf.add_to_end(sentinel, lf.Cell(num))
    new = lf.insert_sort(sentinel)
    lf.iterate(new)


# implement bidirectional methods
def example_bidirect_lists():
    bidir_list = bl.BiList(None)
    list_of_values = [1, 3, 5, 2, 8, 4]
    for num in list_of_values:
        bidir_list.add_head(num)
    print(bidir_list)


# implement a copy function
def example_copy_of_list():
    sentinel = lf.Cell(None)
    list_of_values = [3, 5, 7, 3, 2, 5, 10, 14, 11]
    for num in list_of_values:
        lf.add_to_end(sentinel, lf.Cell(num))
    new = lf.copy_list(sentinel)
    lf.iterate(new)


# implement working with lists with loops. Marking
def example_marking():
    sentinel = ll.Cellv(None)
    list_of_values = [1, 2, 3, 4, 5]
    for num in list_of_values:
        ll.add_to_end(sentinel, ll.Cellv(num))
    ll.has_loop_marking(sentinel)


# implement working with loops. Retracing
def example_retracing():
    sentinel = ll.Cell(None)
    list_of_values = [1, 2, 3, 4, 5]
    for num in list_of_values:
        ll.add_to_end(sentinel, ll.Cell(num))
    make_loop = ll.make_circle(sentinel)
    result = ll.has_loop_retracing(make_loop)
    result2 = ll.has_loop_retracing(sentinel)
    print(result2)
    ll.iterate(sentinel)


# implement working with loop. Reverse
def example_reverse():
    sentinel = ll.Cell(None)
    list_of_values = [1, 2, 3, 4, 5]
    for num in list_of_values:
        ll.add_to_end(sentinel, ll.Cell(num))
    has_not_loop = ll.has_loop_reversing(sentinel)
    print(has_not_loop)
    make_loop = ll.make_circle(sentinel)
    has_loop = ll.has_loop_reversing(make_loop)
    print(has_loop)


# implemet working with loop. Floid Algorithm
def example_floid():
    sentinel = ll.Cell(None)
    list_of_values = [1, 2, 3, 4, 5, 6, 7]
    for num in list_of_values:
        ll.add_to_end(sentinel, ll.Cell(num))
    check_loop = ll.floid_algorithm(sentinel)
    print(check_loop)
    ll.iterate(sentinel)


# release a lists' functions
# release by sentinel and working with one
def example_lists_func():
    sentinel = lf.Cell(None)
    list_of_cells = []
    # filling out the list
    for i in range(0, 10):
        list_of_cells.append(lf.Cell(i))
    for i in range(0, 5):
        lf.add_to_end(sentinel, list_of_cells[i])
    for i in range(5, 10):
        lf.add_to_head(sentinel, list_of_cells[i])
    lf.iterate(sentinel)


# example of releasing loops' methods
def loops():
    print("""You can choose one of below methods of finding loops in cycles:
    1 Retracing
    2 Marking
    3 Floid algorithm
    4 Reversing
    """)
    user_loop = int(input())
    if user_loop == 1:
        example_retracing()
    elif user_loop == 2:
        example_marking()
    elif user_loop == 3:
        example_reverse()
    elif user_loop == 4:
        example_floid()


def menu_of_lists():
    while True:
        print("""Which subpackage are you what to test?
        1 - Release of the binding lists by function and exchanging of cells
        2 - Release of the binding lists by methods
        3 - Release of the working with loops
        4 - Release of the binding bidirectional binding lists 
        5 - Release of the multi-directional binding lists
        0 - Exit
        """)
        user_choice = int(input())
        if user_choice == 1:
            example_lists_func()
        elif user_choice == 2:
            example_list_methods()
        elif user_choice == 3:
            loops()
        elif user_choice == 4:
            example_bidirect_lists()
        elif user_choice == 5:
            print("Fuck off")
        else:
            break


new_menu = inter.Example()
new_menu.mainloop()
