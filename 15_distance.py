"""
Для этого упражнения вам необходимо будет написать программу, которая будет запрашивать у пользователя расстояние в
футах. После этого она должна будет пересчитать это число в дюймы, ярды и мили и вывести на экран. Коэффициенты для
пересчета единиц вы без труда найдете в интернете.
"""
# Код c применением GUI

import PySimpleGUI as psg


def calc_distance(ft):
    ft = float(ft)
    inch = round(ft * 12, 2)
    yard = round(ft / 3, 2)
    miles = round(ft / 5280, 5)
    return [inch, yard, miles]


layout = [[psg.Text("Введите расстояние в футах: "), psg.Input(key="-FT-", size=10)],
          [psg.Button("Расчёт")],
          [psg.Text("В дюймах: "), psg.Text(key="-INCH-")],
          [psg.Text("В ярдах: "), psg.Text(key="-YARD-")],
          [psg.Text("В милях: "), psg.Text(key="-MILES-")],
          [psg.Text(key="-ERROR-", font=("Arial Bold", 30), expand_x=True, colors="#ddaa00", justification="center")]]
window = psg.Window("Distance", layout)

while True:
    event, values = window.read()
    if event != psg.WIN_CLOSED:
        try:
            result = calc_distance(values["-FT-"])
            window["-INCH-"].update(result[0])
            window["-YARD-"].update(result[1])
            window["-MILES-"].update(result[2])
            window["-ERROR-"].update("")
        except ValueError:
            window["-ERROR-"].update("Введите число!")
    else:
        break

# Код без GUI

# def calc_distance(ft):
#     ft = float(ft)
#     inch = round(ft * 12, 2)
#     yard = round(ft / 3, 2)
#     miles = round(ft / 5280, 2)
#     print("В дюймах: {0}\nВ ярдах: {1}\nВ милях: {2}".format(inch, yard, miles))
#
#
# user_ft = input("Введите расстояние в футах: ")
# user_ft = user_ft
# calc_distance(user_ft)
