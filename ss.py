

"""
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


"""
import PySimpleGUI as sg
import pandas as pd


sg.theme('Black')

EXCEL_FILE = 'data_entry.xlsx'
df = pd.read_excel(EXCEL_FILE)

layout = [
[sg.Text('Plaese Fill Out The Following Filed')],# الكلمات الرئيسية لازم تكونتبدأ بحروف كبيرة Text,Combo,..
[sg.Text('Name',size=(15,1)), sg.InputText(key='Name')],
[sg.Text('Favorte Color', size=(15,1)), sg.Combo(['Green','Red','Blue'], key='Favotite Color')],
[sg.Text('I speak', size=(15,1)),
                          sg.Checkbox('Arabic', key='Arabic'),
                          sg.Checkbox('English', key='English'),
                          sg.Checkbox('Italy', key='Italy')],
[sg.Text('No. of children', size=(15,1)), sg.Spin([i for i in range(0,16)],
                                                                   initial_value=0, key='Children')],
[sg.Submit(), sg.Exit()] # زر الراسال وزر الاغلاق
]
window = sg.Window('Simple data entry form',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit': # زر الاغلاق او علامة الاكس
        break # اذا حصل احد الشرطين اللي فوق انهي البرنامج

    if event == 'Submit':  # اذا كان الحدث الضغط على زر  submit يطبع قيمة values
        print(event, values)
window.close()

# https://www.youtube.com/watch?v=svcv8uub0D0
