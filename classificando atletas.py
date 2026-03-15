from datetime import date
ano_atual = date.today().year

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
idade = ano_atual - ano_nascimento
if idade <= 9:
    print('O atleta tem {} anos, ele é da categoria MIRIM.'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos, ele é da categoria INFANTIL.'.format(idade))
elif idade <= 19:
    print(('O atleta tem {} anos, ele é da categoria JUNIOR.'.format(idade)))
else:
    print('O atleta tem {} anos, ele é da categoria SÊNIOR.'.format(idade))

