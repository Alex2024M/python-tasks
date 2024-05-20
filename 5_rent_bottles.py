"""
Во многих странах в стоимость стеклотары закладывается определенный депозит, чтобы стимулировать покупателей напитков
сдавать пустые бутылки. Допустим, бутылки объемом 1 литр и меньше стоят $0,10, а бутылки большего объема – $0,25.

Напишите программу, запрашивающую у пользователя количество бутылок каждого размера. На экране должна отобразиться
сумма, которую можно выручить, если сдать всю имеющуюся посуду. Отформатируйте вывод так, чтобы сумма включала два знака
после запятой и дополнялась слева символом доллара.
"""

amount_less_liter = int(input("Введите количество бутылок объёмом 1 литр и меньше: "))
amount_more_liter = int(input("Введите количество бутылок объёмом больше 1 литра: "))
cost_less_liter = 0.10
cost_more_liter = 0.25

total_price = round((amount_less_liter * cost_less_liter) + (amount_more_liter * cost_more_liter), 2)

print("\nСдана стеклотара на сумму ${0}".format(total_price))
