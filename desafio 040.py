nota1 = float(input('\033[36mQual sua primeira nota? '))
nota2 = float(input('Qual a sua segunda nota? '))
med = (nota1 + nota2) / 2
print('\033[35mSua média é {:.1f}'.format(med))
if med < 5.0:
    print('Seu Resultado: \033[31mREPROVADO')
elif 7 > med >= 5:
    print('Seu Resultado: \033[33mRECUPERAÇÃO')
else:
    print('Seu Resultado: \033[32mAPROVADO')
