num = int(input('digite um número inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opc = int(input('Sua opção: '))
if opc == 1:
    print('{} Convertido  para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opc == 2:
    print('{} Convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opc == 3:
    print('{} Convertido para HEXADECIMAL é igual a {}'.format(
        num, hex(num)[2:]))
else:
    print('Opção inválida, Tente novamente')
