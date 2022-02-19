from random import randint
comp = randint(0, 10)
print("\033[36mSou seu computador, Acabei de pensar em um número entre 0 e 10, tente advinhar! ")
acertou = False
palpites = 0
while not acertou:
    jog = int(input('Qual número você acha que é ? '))
    palpites += 1
    if jog == comp:
        acertou = True
    else:
        if jog < comp:
            print('\033[31mMais...')
        elif jog > comp:
            print('\033[31mMenos...')
if palpites <= 3:
    print('\033[32mVocê acertou com {} tentativas, Parabéns'.format(palpites))
else:
    print('\033[34mVocê acertou com {} tentativas, até a minha vó faria  melhor, tente novamente'.format(palpites))
