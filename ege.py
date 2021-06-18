import PySimpleGUI as sg

sg.theme('Default')   
layout = [  [sg.Text('Всем прив тут вы можете накрутить себе 100 баллов для егэ/гвэ')],
            [sg.Text('Введите кол-во нужных баллов'), sg.InputText()],
            [sg.Text('Введите нужный предмет для накрутки'), sg.InputText()],
            [sg.Button('Накрутить'), sg.Button('Отмена')] ]
window = sg.Window('Накрутка онлайн', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Отмена':
        break
    print('Вы накрутили ', values[0],'баллов егэ, обновите страницу на которой написаны ваши баллы')

window.close()
