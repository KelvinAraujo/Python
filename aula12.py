n = str(input('Qual é o seu nome? '))
if n == 'Kelven':
    print('Que nome bonito!')
elif n == 'Pedro' or n == 'Maria' or n == 'Paulo':
    print('Seu nome é bem popular no brasil')
elif n in "Ana Claudia Jessica Juliana":
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal')
print('tenha um bom dia, {}'.format(n))
