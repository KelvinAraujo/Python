sexo = str(input("Qual seu sexo? [M/F] ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(
        input("Dados inválidos, Digite novamente seu sexo: [M/F] ")).strip().upper()[0]
print('Registrado com sucesso!!')
