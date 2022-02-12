sa = float(input('\033[31mQuanto é o seu salário? R$'))
if sa >= 1250.00:
    print('\033[32m Seu salário com aumento de 10% fica {}'.format(sa + (sa * 10 / 100)))
else:
    print('\033[35m Seu salário com aumento de 15% fica {}'.format(sa + (sa * 15 / 100)))
