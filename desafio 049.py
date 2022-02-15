n = int(input('\033[34m Digite um número para ver a tabuada:\033[m'))
for c in range(1, 11):
    print('\033[35m {} x {:2} = {}'.format(n, c, n * c))
