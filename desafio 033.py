a = int(input('\033[33mPrimeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor =c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('\033[36mo menor é {}'.format(menor))
print('o maior é {}'.format(maior))
