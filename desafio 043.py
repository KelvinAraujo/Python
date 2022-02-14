peso = float(input('\033[35mQual é o seu peso? (Kg) '))
alt = float(input('Qual a sua altura? (m) '))
imc = peso / (alt ** 2)
print('O Seu IMC é de {:.1f} '.format(imc))
if imc < 18.5:
    print('\033[31mvocê está ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('\033[32mVocê está no PESO IDEAL')
elif 25 <= imc < 30:
    print('\033[37mVocê está em SOBRE  PESO')
elif 30 <= imc < 40:
    print('\033[33mVocê está em OBESIDADE, cuidado!')
elif imc > 40:
    print('\033[31mVocê está em OBESIDADE MÓRBIDA')
