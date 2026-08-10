ang1 = float(input('Digite o valor do primeiro ângulo do triangulo: '))
ang2 = float(input('Digite o valor do segundo ângulo do triangulo: '))
ang3 = float(input('Digite o valor do terceiro ângulo do triangulo: '))
if ang1 == ang2 != ang3 or ang1 == ang3 != ang2 or ang2 == ang3 != ang1:
    print('Os ângulos formam um triangulo isosceles. ')
elif ang1 == ang2 or ang1 == ang3 or ang2 == ang3:
    print('Os ângulos formam um triangulo equilatero.')
else:
    ang1 != ang2 != ang3
    print('Os ângulos formam um triangulo escaleno. ')
