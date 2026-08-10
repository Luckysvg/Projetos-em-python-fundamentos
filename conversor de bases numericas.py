num = int(input('Digite um numero inteiro:'))
print('Escolha a base de conversão:')
print('[1] - Binário')
print('[2] - Octal')
print('[3] - Hexadecimal')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))