def test_decorator(arg):
    def wrapper(b):
        print("Hello")
        arg(b)
        print("Bue")
    return wrapper


def func(a):
    print("chmo")
    print(a)


test_decorator(func)(10)
