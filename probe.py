import PySimpleGUI as sg

# layout = [[sg.Text("ROW 1"), sg.Button("Row 1 - #1"), sg.Checkbox("Row 1 - #2"), sg.Button("Row 1 - #3")],
#           [sg.Text("ROW 2"), sg.Checkbox("Row 2 - #1"), sg.Checkbox("Row 2 - #2"), sg.Checkbox("Row 2 - #3")],
#           [sg.Text("ROW 3"), sg.Button("Row 3 - #1"), sg.Button("Row 3 - #2")]]
# window = sg.Window("Probe", layout, size=(600, 300))
#
# while True:
#     event, values = window.read()
#     if event == "Row 1 - #1":
#         print("Ok")
#     if event == sg.WIN_CLOSED:
#         break


layout = [[sg.Text("Network Tester", font="20", colors=("White", "#00002f"))],
          [sg.TabGroup([[
              sg.Tab("Send", [[sg.Text("Message to send:"), sg.Multiline(size=(60, 10), key="SEND")]]),
              sg.Tab("Receive", [[sg.Text("Message Received"), sg.Multiline(size=(60, 10), key="RCV")]])]])],
          [sg.Button("Send Message", button_color=("Black", "LightBlue")), sg.Button("Exit", button_color="Red")]]
window = sg.Window("My Network Tester", layout, sg.theme("DarkBlue18"), use_custom_titlebar=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    if event == "Send Message":
        sg.popup("Sending", values["SEND"])
        window["RCV"].update(values["SEND"])

window.close()
