"""
Многие люди на планете привыкли рассчитывать рост человека в футах и дюймах, даже если в их стране принята метрическая
система. Напишите программу, которая будет запрашивать у пользователя количество футов, а затем дюймов в его росте.
После этого она должна пересчитать рост в сантиметры и вывести его на экран.

Подсказка. Один фут равен 12 дюймам, а один дюйм – 2,54 см.
"""
# Код с использованием GUI
import PySimpleGUI as psg


def calc_height_ft_in_cm(ft):
    ft = float(ft)
    result_ft_cm = round(ft * 12 * 2.54, 2)
    return result_ft_cm


def calc_height_inch_in_cm(inch):
    inch = float(inch)
    result_inch_cm = round(inch * 2.54, 2)
    return result_inch_cm


layout = [[psg.Text("Введите свой рост в футах: ", size=23), psg.Input(key="-FT-", size=10)],
          [psg.Text("Результат перевода футов в см: ", size=26), psg.Text(key="-RESULT_FT-")],
          [psg.Text("Введите свой рост в дюймах: "), psg.Input(key="-INCH-", size=10)],
          [psg.Text("Результат перевода дюймов в см: "), psg.Text(key="-RESULT_INCH-")],
          [psg.Button("Расчёт", bind_return_key=True)]]
window = psg.Window("Conversion height", layout, size=(350, 300))
event, values = window.read()

while True:
    event, values = window.read()
    if event != psg.WIN_CLOSED:
        try:
            if values["-FT-"].isdigit() and values["-INCH-"] == "":
                result_ft = calc_height_ft_in_cm(values["-FT-"])
                window["-RESULT_FT-"].update(result_ft)
            elif values["-INCH-"].isdigit() and values["-FT-"] == "":
                result_inch = calc_height_inch_in_cm(values["-INCH-"])
                window["-RESULT_INCH-"].update(result_inch)
            else:
                result_ft = calc_height_ft_in_cm(values["-FT-"])
                result_inch = calc_height_inch_in_cm(values["-INCH-"])
                window["-RESULT_FT-"].update(result_ft)
                window["-RESULT_INCH-"].update(result_inch)
        except:
            print("Ошибка ввода")
    else:
        break


# Код без GUI
# def calc_height_ft_in_cm(ft):
#     ft = float(ft)
#     result_ft_cm = round(ft * 12 * 2.54, 2)
#     print("Ваш рост составляет {0} футов или {1} см".format(ft, result_ft_cm))
#
#
# def calc_height_inch_in_cm(inch):
#     inch = float(inch)
#     result_inch_cm = round(inch * 2.54, 2)
#     print("Ваш рост составляет {0} дюйм или {1} см".format(inch, result_inch_cm))
#
#
# user_ft = input("Введите свой рост в футах: ")
# user_inch = input("Введите свой рост в дюймах: ")
# print()
#
# if user_ft.isdigit() and user_inch == "":
#     calc_height_ft_in_cm(user_ft)
# elif user_inch.isdigit() and user_ft == "":
#     calc_height_inch_in_cm(user_inch)
# else:
#     calc_height_ft_in_cm(user_ft)
#     calc_height_inch_in_cm(user_inch)
