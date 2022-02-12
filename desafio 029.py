km = int(input('\033[36mQuantos KmH você estava: '))
if km >80:
    print("\033[31mVocê estava acima do limite, você foi multado")
    print('Sua multa é {:.2f}'.format((km-80)*7))
else:
    print('\033[32mVocê estava no limite correto!')
