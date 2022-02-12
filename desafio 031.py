km = float(input('Quantos km tem sua viagem? '))
if km <=200:
    print('O valor da sua viagem é R${:.2f}'.format(km*0.50))
else:
    print('o valor da sua viagem é R${:.2f}'.format(km*0.45))
