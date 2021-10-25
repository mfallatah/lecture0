import PySimpleGUI as sg

sg.theme('darktea19')

layout = [
[sg.Text('Plaese Fill Out The Following Filed')],
[sg.Text('Name',size=(15,1)), sg.InputText(key='Name')],
[sg.Submit(), sg.Exit()]
]
window = sg.Window('Simple data entry form',layout)





# https://www.youtube.com/watch?v=svcv8uub0D0