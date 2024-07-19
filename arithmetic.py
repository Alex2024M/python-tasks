"""
Создайте программу, которая запрашивает у пользователя два целых числа a и b, после чего выводит на экран результаты
следующих математических операций:

- сумма a и b;
- разница между a и b;
- произведение a и b;
- частное от деления a на b;
- остаток от деления a на b;
- десятичный логарифм числа a;
- результат возведения числа a в степень b.
"""
import math


def check_is_number(num):
    while True:
        if not num.isdigit():
            num = input("Введены недопустимые символы. Введите целое число: ")
        else:
            break
    return int(num)


def operation(num_1, num_2):
    summa = num_1 + num_2
    difference = num_1 - num_2
    multiplication = num_1 * num_2
    private_division = num_1 // num_2
    remainder_division = num_1 % num_2
    log = math.log10(num_1)
    degree = num_1 ** num_2
    print("\nСумма {0} и {1}: {2}".format(num_1, num_2, summa))
    print("Разница между {0} и {1}: {2}".format(num_1, num_2, difference))
    print("Произведение {0} и {1}: {2}".format(num_1, num_2, multiplication))
    print("Частное от деления {0} на {1}: {2}".format(num_1, num_2, private_division))
    print("Остаток от деления {0} на {1}: {2}".format(num_1, num_2, remainder_division))
    print("Десятичный логарифм числа {0}: {1}".format(num_1, log))
    print("Результат возведения числа {0} в степень {1}: {2}".format(num_1, num_2, degree))


number_1 = input("Введите первое целое число: ")
number_1 = check_is_number(number_1)
number_2 = input("Введите второе целое число: ")
number_2 = check_is_number(number_2)

operation(number_1, number_2)
