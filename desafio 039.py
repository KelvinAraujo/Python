from datetime import date
atual = date.today().year
nasc = int(input('Qual é o ano do seu nascimento?  '))
idade = atual - nasc
print('Quem nasceu em {} e tem {} anos em {}'.format(nasc, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!!')
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos, faltam {} ano(s) para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('você já deveria ter se alistado há {} ano(s)'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))
