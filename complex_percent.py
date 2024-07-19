"""
Представьте, что вы открыли в банке сберегательный счет под 4% годовых. Проценты банк рассчитывает в конце года и
добавляет к сумме счета.
Напишите программу, которая запрашивает у пользователя сумму первоначального депозита, после чего рассчитывает и выводит
на экран сумму на счету в конце первого, второго и третьего годов. Все суммы должны быть округлены до двух знаков после
запятой.
"""

percent_year = 4
amount_year = 3
initial_deposit = float(input("Введите сумму первоначального депозита: "))

first_year = round(initial_deposit * (percent_year / 100) + initial_deposit, 2)
year = first_year
print("Год 1: {0}".format(first_year))

for num_year in range(2, amount_year + 1):
    year = round(year * (percent_year / 100) + year, 2)
    year = year
    print("Год {0}: {1}".format(num_year, year))
