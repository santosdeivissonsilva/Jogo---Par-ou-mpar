from random import randint

print('-=' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('-=' * 20)

vitoria = 0

while True:
    num = int(input('Digite um valor: '))
    computador = randint(0, 10)
    soma = num + computador
    parimpar = ' '
    while parimpar not in 'PI':
        parimpar = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]
    print('-' * 40)
    if parimpar == 'P':
        if soma % 2 == 0:
            vitoria += 1
            print(
                f'Você jogou {num} e o computador jogou {computador}. Total de {soma} DEU PAR.')
            print('-' * 40)
            print('VOCÊ VENCEU!\nVamos jogar novamente...')
            print('-=' * 20)
        else:
            print(
                f'Você jogou {num} e o computador jogou {computador}. Total de {soma} DEU ÍMPAR.')
            print('-' * 40)
            print('VOCÊ PERDEU!')
            break
    if parimpar == 'I':
        if soma % 2 != 0:
            vitoria += 1
            print(
                f'Você jogou {num} e o computador jogou {computador}. Total de {soma} DEU ÍMPAR.')
            print('-' * 40)
            print('VOCÊ VENCEU!\nVamos jogar novamente...')
            print('-=' * 20)
        else:
            print(
                f'Você jogou {num} e o computador jogou {computador}. Total de {soma} DEU PAR.')
            print('-' * 40)
            print('VOCÊ PERDEU!')
            break

print('-=' * 20)
print(f'GAME OVER! Você venceu {vitoria} vezes.')
