"""
Интернет-магазин занимается продажей различных сувениров и безделушек. Каждый сувенир весит 75 г, а безделушка – 112 г.
Напишите программу, запрашивающую у пользователя количество тех и других покупок, после чего выведите на экран общий вес
посылки.
"""

weight_souvenir = 75
weight_bauble = 112
amount_souvenir = input("Введите количество сувениров: ")
amount_bauble = input("Введите количество безделушек: ")

while True:
    if not amount_souvenir.isdigit():
        amount_souvenir = input("Введите количество сувениров: ")
    elif not amount_bauble.isdigit():
        amount_bauble = input("Введите количество безделушек: ")
    else:
        break

total_weight = (int(amount_souvenir) * weight_souvenir) + (int(amount_bauble) * weight_bauble)

print("\nОбщий вес посылки: {0} грамм".format(total_weight))
