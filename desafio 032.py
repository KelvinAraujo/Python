from datetime import date
ano = int(input('\033[31m Qual ano quer analisar? Digite 0 para o ano atual '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('\033[35m O ano {} é BISSSEXTO!'.format(ano))
else:
    print('\033[33m O ano {} Não é BISSEXTO!'.format(ano))
