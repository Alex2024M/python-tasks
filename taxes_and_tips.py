"""
Программа, которую вы напишете, должна начинаться с запроса у пользователя суммы заказа в ресторане. После этого
должен быть произведен расчет налога и чаевых официанту. Вы можете использовать принятую в вашем регионе налоговую
ставку для подсчета суммы сборов. В качестве чаевых мы оставим 18 % от стоимости заказа без учета налога. На выходе
программа должна отобразить отдельно налог, сумму чаевых и итог, включая обе составляющие. Форматируйте вывод таким
образом, чтобы все числа отображались с двумя знаками после запятой.
"""

sum_order = float(input("Введите сумму заказа: "))
tax_percent = 13
tips_percent = 18

tax = round(sum_order * (tax_percent / 100), 2)
tips = round(sum_order * (tips_percent / 100), 2)
total_sum = round(sum_order + tax + tips, 2)

print("\nНалог с заказа: {0}".format(tax))
print("Чаевые с заказа: {0}".format(tips))
print("Общая сумма заказа с налогом и чаевыми: {0}".format(total_sum))