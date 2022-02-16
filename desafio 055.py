maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input('\033[34mQual o peso da {} pessoa: '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('\033[32mO maior peso foi {}'.format(maior))
print('O menor peso foi {}'.format(menor))
