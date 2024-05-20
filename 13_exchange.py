"""
Представьте, что вы пишете программное обеспечение для автоматической кассы в магазине самообслуживания. Одной из
функций, заложенных в кассу, должен быть расчет сдачи в случае оплаты покупателем наличными.

Напишите программу, которая будет запрашивать у пользователя сумму сдачи в центах. После этого она должна рассчитать и
вывести на экран, сколько и каких монет потребуется для выдачи указанной суммы, при условии что должно быть
задействовано минимально возможное количество монет. Допустим, у нас есть в распоряжении монеты достоинством в 1,
5, 10, 25 центов, а также в 1 (loonie) и 2 (toonie) канадских доллара.

Примечание. Монета номиналом в 1 доллар была выпущена в Канаде в 1987 году. Свое просторечное название (loonie) она
получила от изображения полярной гагары (loon) на ней. Двухдолларовая монета, вышедшая девятью годами позже, была про-
звана toonie, как комбинация из слов два (two) и loonie.
"""


def change_calculation(cent):
    coin_denomination = (25, 10, 5, 1)
    min_coins = []
    count = {}
    for nominal in coin_denomination:
        while cent >= nominal:
            if cent // nominal != 0:
                min_coins.append(nominal)
                cent -= nominal
    for coin in min_coins:
        if coin not in count:
            count[coin] = 1
        else:
            count[coin] += 1
    return count


def check_exception():
    while True:
        try:
            check_cent = int(input("Введите сумму сдачи в центах: "))
            print()
        except ValueError:
            print("Введено дробное число или другие символы! Введите целое число.\n")
        else:
            return check_cent


change_cent = check_exception()
result = change_calculation(change_cent)
print("Для сдачи {0} цент потребуется:".format(format(change_cent)))
for denomination, count_coins in result.items():
    print("\t{0} цент в количестве {1} штук".format(denomination, count_coins))
