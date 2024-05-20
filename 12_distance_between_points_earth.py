"""
Как известно, поверхность планеты Земля искривлена, и расстояние между точками, характеризующимися одинаковыми градусами
по долготе, может быть разным в зависимости от широты. Таким образом, для вычисления расстояния между двумя точками на
Земле одной лишь теоремой Пифагора не обойтись.

Допустим, (t1, g1) и (t2, g2) – координаты широты и долготы двух точек на поверхности Земли. Тогда расстояние в
километрах между ними с учетом искривленности планеты можно найти по следующей формуле:
distance = 6371,01 * arccos(sin(t1) * sin(t2) + cos(t1) * cos(t2) * cos(g1 - g2)).

Примечание. Число 6371,01 в этой формуле, конечно, было выбрано не случайно и представляет собой среднее значение
радиуса Земли в километрах.

Напишите программу, в которой пользователь будет вводить координаты двух точек на Земле (широту и долготу) в градусах.
На выходе мы должны получить расстояние между этими точками при следовании по кратчайшему пути по поверхности планеты.

Подсказка. Тригонометрические функции в Python оперируют радианами. Таким образом, вам придется введенные пользователем
величины из градусов перевести в радианы, прежде чем вычислять расстояние между точками. В модуле math есть удобная
функция с названием radians-Функции:radians, служащая как раз для перевода градусов в радианы.
"""

import math


def check_exception_latitude():
    while True:
        try:
            user_lat = math.radians(float(input("Введите широту в градусах: ")))
        except ValueError:
            print("Неверные данные. Введено не число\n")
        else:
            return user_lat


def check_exception_longitude():
    while True:
        try:
            user_long = math.radians(float(input("Введите долготу в градусах: ")))
        except ValueError:
            print("Неверные данные. Введено не число\n")
        else:
            return user_long


def coordinate_two_point():
    coordinate = []
    for number in range(1, 3):
        print("Введите координты {} точки".format(number))
        for i_coord in range(1):
            user_latitude = check_exception_latitude()
            user_longitude = check_exception_longitude()
            coordinate.append((user_latitude, user_longitude))
        print()

    return coordinate


def calculate_distance(coordinate):
    sinus_0_0 = math.sin(coordinate[0][0])
    sinus_1_0 = math.sin(coordinate[1][0])
    cosine_0_0 = math.cos(coordinate[0][0])
    cosine_1_0 = math.cos(coordinate[1][0])
    cosine_0_1 = math.cos(coordinate[0][1] - coordinate[1][1])
    distance = round(6371.01 * math.acos(sinus_0_0 * sinus_1_0 + cosine_0_0 * cosine_1_0 * cosine_0_1), 2)

    return "Расстояние между введёными точками: {}".format(distance)


coordinate_points = coordinate_two_point()
result_distance = calculate_distance(coordinate_points)
print(result_distance)
