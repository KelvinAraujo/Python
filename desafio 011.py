l = float(input('\033[33m largura da parede:'))
a = float(input('\033[35m altura da parede:'))
are = l * a
print('A sua parede tem dimensão de {}m x {}m e a sua area é de {}m²'.format(l, a, are))
t = are / 2
print('Para pintar esta parede você precisa de {:.2f}L de tinta'.format(t))
Testando...
