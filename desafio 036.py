vdc = int(input('\033[33mQual o valor da casa? R$'))
sal = float(input('Quanto é o seu salário? R$'))
qda = int(input('Em quantos anos você vai pagar? '))
p = qda * 12
pre = vdc / p
if pre > (sal * 30 / 100):
    print('\033[31mvocê não pode fazer este empréstimo pois o valor da prestação ultrapassa 30% do seu salário!')
else:
    print('\033[32mParábens seu empréstimo foi aprovado!')
print('Valor da prestação: R${:.2f} por mês'.format(pre))
