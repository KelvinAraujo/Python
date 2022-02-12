import math
angulo = float(input('\033[35m Digite o angulo que você deseja: '))
seno = math.sin(math.radians(angulo))
print('\033[31m o angulo de {}º tem o seno de {:.2f}'.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('O angulo de {}º tem o cosseno de {:.2f}'.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('O angulo de {}º tem a tangente de {:.2f}'.format(angulo, tangente))
