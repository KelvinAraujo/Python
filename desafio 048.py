soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('\033[32mA soma de todos os {} valores é {}'.format(cont, soma))
