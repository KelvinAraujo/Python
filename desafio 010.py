n = float(input('\033[31m quanto você tem? R$'))
d = n / 5.30
e = n / 6.05
print('\033[36m Com R${} Reais você compra \033[32mUS${:.2f} Doláres e \033[34m£{:.2f} Euros'.format(n,d,e))
