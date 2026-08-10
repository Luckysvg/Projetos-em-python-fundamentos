maior_idade = 0
menor_idade = 0
media_idade = 0

for pess in range(1, 5):
    nome = input('Digite o nome da {} pessoa: '.format(pess))
    idade = int(input('Digite a idade da {} pessoa: '.format(pess)))
    sexo = input('Digite o sexo da {} pessoa (M/F): '.format(pess)).upper()

    media_idade += idade

    if idade > maior_idade:
        maior_idade = idade

    if idade < menor_idade or menor_idade == 0:
        menor_idade = idade

print('A média de idade do grupo é de {} anos.'.format(media_idade / 4))
print('O homem mais velho tem {} anos.'.format(maior_idade))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(menor_idade))


            

           


              

                    
