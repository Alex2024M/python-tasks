"""
В США потребление автомобильного топлива исчисляется в милях на галлон (miles-per-gallon – MPG). В то же время в Канаде
этот показатель обычно выражается в литрах на 100 км (liters-per-hundred kilometers – L/100 km). Используйте свои
исследовательские способности, чтобы определить формулу перевода первых единиц исчисления в последние. После
этого напишите программу, запрашивающую у пользователя показатель потребления топлива автомобилем в американских
единицах и выводящую его на экран в канадских единицах.
"""


def check_is_number(miles_gal):
    while True:
        if not miles_gal.isdigit():
            miles_gal = input("Неверные символы. Введите расход топлива в американских галлонах: ")
        else:
            break
    return int(miles_gal)


def calculation(miles_gal):
    liters_100km = 235.21 / miles_gal
    print("Расход топлива в канадских единицах: {}л/100км".format(round(liters_100km, 1)))


mpg = input("Введите расход топлива в американских галлонах: ")
mpg = check_is_number(mpg)
calculation(mpg)
