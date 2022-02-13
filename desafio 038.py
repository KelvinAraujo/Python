n1 = int(input('\033[37mDigite um número inteiro: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('\033[32mO número {} é maior!'.format(n1))
elif n2 > n1:
    print('\033[35mO número {} é maior!'.format(n2))
else:
    print('\033[36mOs dois núemros são iguais!!')
