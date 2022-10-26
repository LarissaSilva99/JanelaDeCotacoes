import PySimpleGUI as sg
from cotacao import pegar_cotacoes


layout = [
    [sg.Text('Pegar cotação da moeda')],
    [sg.InputText(key='nome_cotacao')],
    [sg.Button('Pegar'), sg.Button('Cancelar')],
    [sg.Text('', key='texto_cotacao')],
]

janela = sg.Window('Sistema de cotaçoes:', layout)

while True:
    # evento é todo clique que fizer dentro da janela
    # valor é sempre que preeencher um lugar com algo
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED or evento == 'Cancelar':
        break
    if evento == 'Pegar':
        codigo_cotacao = valores['nome_cotacao']
        cotacao = pegar_cotacoes(codigo_cotacao)
        print(f'A cotação do {codigo_cotacao} é de R$ {cotacao}')

janela.close()