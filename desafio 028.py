from random import randint
from time import sleep
comp = randint(0,5)
print('\033[31m-=' * 20)
print('\033[32mEu pensei em um número entre 0 e 5, tente advinhar...')
print('\033[31m-=' * 20)
jog = int(input('\033[32mEm que número eu pensei? '))
print('\033[33mPROCESSANDO...')
sleep(2)
if jog == comp:
    print('\033[35mPARABÉNS!! Você me venceu!')
else:
    print('\033[34mGANHEI!!! Eu pensei no número {}'.format(comp))
