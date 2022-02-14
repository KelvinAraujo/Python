print('{:^40}'.format('\033[35mLOJAS GUANABARA'))
preço = float(input('\033[32mPreço das compras? R$'))
print('''\033[34mformas de pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão\033[m''')
opc = int(input('\033[32mQual a opção? '))
if opc == 1:
    total = preço - (preço * 10 / 100)
elif opc == 2:
    total = preço - (preço * 5 / 100)
elif opc == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opc == 4:
    total = preço + (preço * 20 / 100)
    topa = int(input('Em quantas vezes? '))
    parcela = total / topa
    print('Sua compra será parcelada em {}x de R${:.2f} com juros'.format(topa, parcela))
else:
    print('\033[31mOpção de pagamento inválida, tente novamente!')
print('\033[36mSua compra de R${:.2f} vai custar R${:.2f} no final.'.format(
    preço, total))
