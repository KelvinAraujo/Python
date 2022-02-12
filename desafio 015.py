p1 = int(input('\033[34m Quantos dias o carro foi alugado? '))
p2 = float(input('\033[34m Quantos km foram rodados? '))
pre1 = p1 * 60
pre2 = p2 * 0.15
preço = pre1 + pre2
print('\033[33m O total a pagar é de: R${:.2f}'.format(preço))
