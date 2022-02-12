r1 = float(input('\033[35mPrimeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos podem formar triângulo!!')
else:
    print('Os segmentos Não podem formar triângulo!!')
