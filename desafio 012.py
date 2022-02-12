preço = float(input("Qual é o preço do produto? R$"))
novo = preço - (preço * 5 / 100)
print('\033[31m O produto que custava R${:.2f}, na Promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
