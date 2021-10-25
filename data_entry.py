
import PySimpleGUI as sg
import pandas as pd


sg.theme('Black')

layout = [
[sg.Text('Plaese Fill Out The Following Filed')],
[sg.Text('Name',size=(15,1)), sg.InputText(key='Name')],
[sg.Submit(), sg.Exit()]
]
window = sg.Window('Simple data entry form',layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Submit':
        print(event, values)        
window.close()
