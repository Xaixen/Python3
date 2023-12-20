import PySimpleGUI as sg
from codigo import cotaçoes
layout = [
    [sg.Text('Pegar cotações')],
    [sg.InputText(key='nome')],
    [sg.Button('Pegar'), sg.Button('Fechar')],
    [sg.Text('', key='texto_cotaçao')]
]

interface = sg.Window('Ttulo da Janela', layout)
while True:
    clique, valores = interface.read()
    if clique == sg.WINDOW_CLOSED or clique == 'Fechar':
        break
    if clique == 'Pegar':
        moeda = valores['nome']
        interface['texto_cotaçao'].update(cotaçoes(moeda))
interface.close()