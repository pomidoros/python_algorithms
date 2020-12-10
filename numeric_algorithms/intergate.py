#I should use here pip
import matplotlib.pyplot as plt
import numpy as np
import math


def draw_figure(f, x1, x2, rule):
    axis_array = np.zeros((2,))
    x_vector = np.array([x1, x2])
    if rule == 'rect':
        y_vector = np.array([f(x1), f(x1)])
    elif rule == 'trap':
        y_vector = np.array([f(x1), f(x2)])
    plt.plot(x_vector, y_vector)
    plt.fill_between(x_vector, y_vector, axis_array)


def use_rectangle_rule(func, xmin, xmax, num_intervals):
    dx = (xmax - xmin) / num_intervals
    x = xmin
    area = 0
    for i in range(1, num_intervals + 1):
        draw_figure(func, x, x + dx, 'rect')
        area += dx * func(x)
        x += dx
    print(f"Total area equal {round(area, 2)}")


def use_trapezoid_rule(func, xmin, xmax, num_intervals):
    dx = (xmax - xmin) / num_intervals
    x = xmin
    area = 0
    axis_array = np.zeros((2,))
    for i in range(1, num_intervals + 1):
        draw_figure(func, x, x + dx, 'trap')
        area += dx * (func(x) + func(x + dx)) / 2
        x += dx
    print(f"Total area equal {round(area, 2)}")


def slice_area(f, x1, x2):
    area = (x2 - x1) * (f(x2) + f(x1)) / 2
    return area


def slice_handling(f, x1, x2, error):
    xm = (x2 + x1) / 2
    total_area = slice_area(f, x1, x2)
    first_area = slice_area(f, x1, xm)
    second_area = slice_area(f, xm, x2)
    return_area = 0
    if abs(1 - total_area / (first_area + second_area)) > error:
        a1 = slice_handling(f, x1, xm, error)
        a2 = slice_handling(f, xm, x2, error)
        return_area = a1 + a2
    else:
        draw_figure(f, x1, x2, 'trap')
        return_area = total_area
    return return_area


def integrate_adapt(func, xmin, xmax, num_intervals, slice_error):
    dx = (xmax - xmin) / num_intervals
    x = xmin
    result_area = 0
    for i in range(1, num_intervals + 1):
        result_area += slice_handling(func, x, x + dx, slice_error)
        x += dx
    print(f"Total area equal {round(result_area, 2)}")


def main(u_input):
    #curve for integrate
    f = lambda x: math.sin(2 * x) + x + 1

    # array of X-axis points
    main_x = np.linspace(0, 5, 100)

    #array of Y-axis points
    y_array = np.sin(2 * main_x) + main_x + np.ones_like(main_x)

    plt.plot(main_x, y_array)

    #first coordinate
    x_coord_min = 0

    #second coordinate
    x_coord_max = 10

    #amount of intervals which devide the area under curve
    # not matter for intergate adapt, but matter for rectangular and
    # trapezoid methods
    n_intervals = 3

    # error of integrate adapt method
    error_area = 0.001

    if u_input == 1:
        use_rectangle_rule(f, x_coord_min, x_coord_max, n_intervals)
    elif u_input == 2:
        use_trapezoid_rule(f, x_coord_min, x_coord_max, n_intervals)
    elif u_input == 3:
        integrate_adapt(f, x_coord_min, x_coord_max, n_intervals, error_area)
    plt.show()


#menu
while True:
    print("""Input the type of approximate method: 
    1. Rectangular method
    2. Trapezoid method
    3. Integrate adapt
    0. Exit""")
    choice = int(input())
    if choice == 1:
        main(1)
    elif choice == 2:
        main(2)
    elif choice == 3:
        main(3)
    elif choice == 0:
        break

