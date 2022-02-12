frase = str(input('\033[35m Digite uma frase: ')).upper().strip()
print('\033[34m A letra A aparece {} vezes na frase'.format(frase.count('A')))
print("A primeira letra A aparece na posição {}".format(frase.find('A')+1))
print('A ultima letra A aparece na posição {}'.format(frase.rfind('A')+1))