frase = str(input('\033[32mDigite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('\033[35mA frase é um palíndromo!')
else:
    print('\033[31mA frase não é um palíndromo!!')
