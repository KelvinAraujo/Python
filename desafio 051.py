primeiro = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
for c in range(primeiro, primeiro + 10 * raz, raz):
  print(c, end=' => ')
  