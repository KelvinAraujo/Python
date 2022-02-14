from random import randint
itens = ('\033[36mPapel', 'Pedra', 'Tesoura')
comp = randint(0, 2)
print('''Suas opções:
[ 1 ] PEDRA
[ 2 ] PAPEL
[ 3 ] TESOURA''')
jog = int(input('Qual é a sua jogada? '))
print('-=' * 11)
print('O Computador jogou {}'.format(itens[comp]))
print('o Jogador jogou {}'.format(itens[jog]))
print('-=' * 11)
if comp == 0:  # Pedra
    if jog == 0:
        print('EMPATE')
    elif jog == 1:
        print('JOGADOR VENCEU!')
    elif jog == 2:
        print('COMPUTADOR VENCEU!')

    else:
        print('Jogada inválida')
elif comp == 1:  # Papel
    if jog == 0:
        print('COMPUTADOR VENCEU!')
    elif jog == 1:
        print('EMPATE')
    elif jog == 2:
        print('JOGADOR VENCEU')
    else:
        print('Jogada inválida')
elif comp == 2:  # Tesoura
    if jog == 0:
        prnt('JOGADOR VENCEU!')
    elif jog == 1:
        print('COMPUTADOR VENCE!')
    elif jog == 2:
        print('EMPATE')
    else:
        print('Jogada inválida')
