num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[m')
        print('{} '.format(c), end=' ')
        print('\n\033[mO número {} foi divisível {} vezes.'.format(num, c))
        if c == 2:
            print('Por isso o número é primo! ')
        else:
            print('Por isso o número não é primo! ')
