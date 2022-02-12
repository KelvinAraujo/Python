import math
co = float(input('\033[36m Comprimento do cateto oposto: '))
ca = float(input('Compriment do cateto adjacente: '))
hi = math.hypot(co, ca)
print('\033[31m A hipotenusa vai medir {:.2f}'.format(hi))


"""co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimneto do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))"""
