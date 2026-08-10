peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f}, você está abaixo do peso.'.format(imc))
elif imc < 25:
    print('Seu IMC é de {:.1f}, você está com o peso ideal.'.format(imc))
elif imc < 30:
    print('Seu IMC é de {:.1f}, você está com sobrepeso.'.format(imc))
elif imc < 40:
    print('Seu IMC é de {:.1f}, você está com obesidade.'.format(imc))
else:
    print('Seu IMC é de {:.1f}, você está com obesidade mórbida.'.format(imc))