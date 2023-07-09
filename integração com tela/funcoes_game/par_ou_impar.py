from random import randint


def JogarParImpar(valor, escolha):
    valor = int(valor)
    computador = randint(0, 10)
    soma = valor + computador

    if escolha == 'Par':
        if soma % 2 == 0:
            print(
                f'Você jogou {valor} e o computador jogou {computador}. Total de {soma} DEU PAR.')
            print('VOCÊ VENCEU!\n')
            print('-='*20)
        else:
            print(
                f'Você jogou {valor} e o computador jogou {computador}. Total de {soma} DEU ÍMPAR.')
            print('VOCÊ PERDEU!')
            print('-='*20)
    if escolha == 'Ímpar':
        if soma % 2 != 0:
            print(
                f'Você jogou {valor} e o computador jogou {computador}. Total de {soma} DEU ÍMPAR.')
            print('VOCÊ VENCEU!\n')
            print('-='*20)
        else:
            print(
                f'Você jogou {valor} e o computador jogou {computador}. Total de {soma} DEU PAR.')
            print('VOCÊ PERDEU!')
            print('-='*20)
