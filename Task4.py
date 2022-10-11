import math


def find_distance(a, b):
    sum_of_diffs = 0
    for i in range(len(a)):
        sum_of_diffs += (a[i] - b[i]) ** 2
    return math.sqrt(sum_of_diffs)


def input_coordinates(n, name):
    a = []
    for i in range(n):
        try:
            a.append(float(input(f'{name}: Введите {i + 1}-ю координату: ')))
        except ValueError:
            return False
    return a


try:
    dimensions = int(input('Введите размерность пространства (целое число): '))
    if dimensions < 1:
        print('Размерность пространства должна быть положительным числом.')
    else:
        point_a = input_coordinates(dimensions, 'Точка А')
        if point_a is False:
            print('Координаты точки должны быть числами, Вы ввели что-то другое.')
        else:
            point_b = input_coordinates(dimensions, 'Точка B')
            if point_b is False:
                print('Координаты точки должны быть числами, Вы ввели что-то другое.')
            else:
                print(f'{point_a}, {point_b} - {find_distance(point_a, point_b)}')
except ValueError:
    print('Размерность пространства должна быть целом числом, Вы ввели что-то другое.')
