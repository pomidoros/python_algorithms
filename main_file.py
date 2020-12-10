#unidirectional list methods package
from lists import list_methods as ul
#bidirectional list methods package
from lists import bidirectional_list_methods as bl
#list functions
from lists import list_func as lf
#list with loop functions
from lists import lists_with_loop as ll

#release a lists' functions
"""
sentinel = lf.Cell(None)
list_of_cells = []
for i in range(0, 10):
    list_of_cells.append(lf.Cell(i))
for i in range(0, 5):
    lf.add_to_end(sentinel, list_of_cells[i])
for i in range(5, 10):
    lf.add_to_head(sentinel, list_of_cells[i])
lf.iterate(sentinel)
"""


#test sorting
"""
sentinel = lf.Cell(None)
list_of_values = [3, 5, 7, 3, 2, 5, 10, 14, 11]
for num in list_of_values:
    lf.add_to_end(sentinel, lf.Cell(num))
new = lf.insert_sort(sentinel)
lf.iterate(new)
"""

# implement a copy function
"""
sentinel = lf.Cell(None)
list_of_values = [3, 5, 7, 3, 2, 5, 10, 14, 11]
for num in list_of_values:
    lf.add_to_end(sentinel, lf.Cell(num))
new = lf.copy_list(sentinel)
lf.iterate(new)
"""

#impleent working with lists with loops. Marking
"""
sentinel = ll.Cellv(None)
list_of_values = [1, 2, 3, 4, 5]
for num in list_of_values:
    ll.add_to_end(sentinel, ll.Cellv(num))
result = ll.has_loop_marking(sentinel)
"""


#implement working with loops. Retracing
"""
sentinel = ll.Cell(None)
list_of_values = [1, 2, 3, 4, 5]
for num in list_of_values:
    ll.add_to_end(sentinel, ll.Cell(num))
make_loop = ll.make_circle(sentinel)
result = ll.has_loop_retracing(make_loop)
result2 = ll.has_loop_retracing(sentinel)
print(result2)
ll.iterate(sentinel)
"""


#implement working with loop. Reverse
"""
sentinel = ll.Cell(None)
list_of_values = [1, 2, 3, 4, 5]
for num in list_of_values:
    ll.add_to_end(sentinel, ll.Cell(num))
has_not_loop = ll.has_loop_reversing(sentinel)
print(has_not_loop)
make_loop = ll.make_circle(sentinel)
has_loop = ll.has_loop_reversing(make_loop)
print(has_loop)
"""

#implemet working with loop. Floid Algorithm
sentinel = ll.Cell(None)
list_of_values = [1, 2, 3, 4, 5, 6, 7]
for num in list_of_values:
    ll.add_to_end(sentinel, ll.Cell(num))
check_loop = ll.floid_algorithm(sentinel)
print(check_loop)
ll.iterate(sentinel)


def menu_of_lists():
    while True:
        print("""Which subpackage are you what to test?
        1. Release of the binding lists by function and exchanging of cells
        2. Release of the binding lists by methods
        3. Release of the working with loops
        4. Release of the binding bidirectional binding lists 
        5. Release of the multi-directional binding lists
        0. Exit
        """)
        user_choice = int(input())
        if user_choice == 1:
            pass
        elif user_choice == 2:
            pass
        elif user_choice == 3:
            pass
        elif user_choice == 4:
            pass
        elif user_choice == 5:
            pass
        else:
            break
