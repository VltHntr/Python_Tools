import PySimpleGUI as sg

layout = [[sg.Text(text="YouTube Download")],
          [sg.Text(text="URL: "), sg.InputText()],
          [sg.Button("Download"), sg.Button("Cancel")]
]

window = sg.Window(title="YouTube Download", layout=layout)

while True:
    events, value = window.read()

    if events == sg.WIN_CLOSED or events == "Cancel":
        break

    if events == "Download":
        sg.Popup(title="SUCCESS")

window.close()