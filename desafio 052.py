n = int(input('Digite um número: '))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
        print('\033[33m', end='')
    else:
        print('\033[31m', end='')
    print('{}'.format(c), end='')
print('\n\033[36mO número {} foi divisivel {} vezes'.format(n, tot))
if tot == 2:
    print('\033[32mPor isso ele é PRIMO!')
else:
    print('\033[31mPor isso ele NÃO é PRIMO ')
