import PySimpleGUI as sg
import funcoes_game.par_ou_impar as jpi


class Tela:
    def __init__(self):
        # Layout
        layout = [
            [sg.Text('VAMOS JOGAR PAR OU ÍMPAR?')],
            [sg.Text('Digite um valor: '), sg.InputText(
                size=5, focus=True, key='numero')],
            [sg.Combo(['Par', 'Ímpar'], key='escolha')],
            [sg.Button('Ok')],
            [sg.Output(size=(70, 20))],
        ]

        # Janela
        self.janela = sg.Window('Jogo - Par ou Ímpar', layout, size=(500, 300))

    def Iniciar(self):
        while True:
            # Extrair os dados da tela
            self.button, self.valores = self.janela.Read()
            numero = self.valores['numero']
            escolha = self.valores['escolha']
            jpi.JogarParImpar(numero, escolha)


tela = Tela()
tela.Iniciar()
