salario = float(input('\033[32m Quanto é o salário? R$'))
novo = salario + (salario * 15 / 100)
print('\033[36m Um funcionário que ganhava R${:.2f}, com aumento de 15% agora recebe R${:.2f}'.format(salario,novo))
