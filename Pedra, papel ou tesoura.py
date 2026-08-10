from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
escolha_computador = randint(0, 2)
print('Suas opções:' \
' [0] PEDRA' \
' [1] PAPEL' \
' [2] TESOURA')
jogador = int(input('Qual é a sua jogada?  '))
print('-=' * 11)
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[escolha_computador]))
if escolha_computador == 0:
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCEU!')
    else:
        print('COMPUTADOR VENCEU!')
elif escolha_computador == 1:
    if jogador == 0:
        print('COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!')
    else:
        print('JOGADOR VENCEU!')
else:
    if jogador == 0:
        print('JOGADOR VENCEU!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!')
    else:
        print('EMPATE!')