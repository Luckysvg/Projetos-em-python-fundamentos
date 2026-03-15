from datetime import date
ano_atual = date.today().year
ano_nascimento = int(input('Digite o ano de nascimento: '))
idade = ano_atual - ano_nascimento
if idade < 18:
    print('Ainda faltam {} anos para o alistamento, por enquanto, você está dispensado por enquanto.'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar, procure o posto de alistamento mais próximo de você.')
else:
    print('Você já deveria ter se alistado há {} anos, procure pelo posto de alistamento mais próximo de você.'.format(idade - 18))
