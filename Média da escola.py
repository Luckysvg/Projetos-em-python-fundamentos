num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
média = (num1 + num2) /2
print('A média entre {} e {} é igual a {}'.format(num1, num2, média))
if média < 5:
    print('Você está reprovado!')
elif média >= 5 and média < 7:
    print('Você está de recuperação!')
else:
    print('Você está aprovado! Parabéns!')

  

    
