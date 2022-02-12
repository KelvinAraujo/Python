c = int(input('\033[31m Informe a temperatura em ºC:'))
f = c * 1.8 + 32
print('\033[34m {}ºC corresponde a {:.0f}ºF em fahrenheit'.format(c,f))
