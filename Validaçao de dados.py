sexo = input('Digite o sexo da pessoa (M/F): ').strip().upper()

while sexo not in ['M', 'F']:
    print('Sexo inválido.')
    sexo = input('Digite novamente (M/F): ').strip().upper()

print('Sexo válido, digite novamente: ', sexo)