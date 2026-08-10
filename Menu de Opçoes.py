n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opçao = 0
while opçao != 5:
    print('''  [1] Somar
  [2] Subtrair
  [3] Maior
  [4] novos números
  [5] Sair''')
    opçao = int(input('Escolha uma opção: '))
    if opçao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, soma))
    elif opçao == 2:
        subtracao = n1 - n2
        print('A subtração entre {} e {} é igual a {}'.format(n1, n2, subtracao))
    elif opçao == 3:
        if n1 > n2:
            print('O maior valor entre {} e {} é {}'.format(n1, n2, n1))
        else:
            print('O maior valor entre {} e {} é {}'.format(n1, n2, n2))
    elif opçao == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

print('Fim do programa! Volte sempre!')