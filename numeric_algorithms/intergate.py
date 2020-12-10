#I should use here pip
import matplotlib.pyplot as plt
import numpy as np
import math


def use_rectangle_rule(func, xmin, xmax, num_intervals):
    dx = (xmax - xmin) / num_intervals
    x = xmin
    area = 0
    axis_array = np.zeros((2,))
    for i in range(1, num_intervals + 1):
        x_vector = np.array([x, x + dx])
        y_vector = np.array([func(x), func(x)])
        plt.plot(x_vector, y_vector)
        plt.fill_between(x_vector, y_vector, axis_array)
        area += dx * func(x)
        x += dx
    print(f"Total area equal {round(area, 2)}")


def use_trapezoid_rule(func, xmin, xmax, num_intervals):
    dx = (xmax - xmin) / num_intervals
    x = xmin
    area = 0
    axis_array = np.zeros((2,))
    for i in range(1, num_intervals + 1):
        x_vector = np.array([x, x + dx])
        y_vector = np.array([func(x), func(x + dx)])
        plt.plot(x_vector, y_vector)
        plt.fill_between(x_vector, y_vector, axis_array)
        area += dx * (func(x) + func(x + dx)) / 2
        x += dx
    print(f"Total area equal {round(area, 2)}")


def integrate_adapt(func, xmin, xmax, num_intervals, slice_error):
    pass


def main(u_input):
    f = lambda x: math.sin(2 * x) + x + 1
    main_x = np.linspace(0, 5, 100)
    y_array = np.sin(2 * main_x) + main_x + np.ones_like(main_x)
    plt.plot(main_x, y_array)

    x_coord_min = 0
    x_coord_max = 5
    n_intervals = 10

    if u_input == 1:
        use_rectangle_rule(f, x_coord_min, x_coord_max, n_intervals)
    elif u_input == 2:
        use_trapezoid_rule(f, x_coord_min, x_coord_max, n_intervals)
    plt.show()


while True:
    print("""Input the type of approximate method: 
    1. Rectangular method
    2. Trapezoid method
    0. Exit""")
    choice = int(input())
    if choice == 1:
        main(1)
    elif choice == 2:
        main(2)
    elif choice == 3:
        break

