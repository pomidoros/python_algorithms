from list.list_methods import List
from list.lists_with_loops import CList
from colorama import Style, Fore


class GoBeyondException(Exception):
    pass


class FloatException(Exception):
    pass


def make_exception(string):
    return Fore.RED + string + Style.RESET_ALL


print(Fore.GREEN + "Welcome" + Style.RESET_ALL + "\n")
while True:
    print("""Choose the type of list which you want to create:
    1. Thr usual list
    2. The list with loop""")
    try:
        user_input = int(input("Your choice: "))
        if user_input != round(user_input):
            raise FloatException(make_exception("\nInput the integer number\n"))
        if user_input < 0 or user_input > 2:
            raise GoBeyondException(make_exception("\nInput the correct number\n"))
    except ValueError:
        print(make_exception("\nInput the integer number\n"))
        continue
    except (GoBeyondException, FloatException) as exc:
        print(exc)
    else:
        if user_input == 1:
            new_list = List()
        elif user_input == 2:
            new_list = CList()
        elif user_input == 0:
            break

print(Fore.GREEN + "\nBye" + Style.RESET_ALL)
