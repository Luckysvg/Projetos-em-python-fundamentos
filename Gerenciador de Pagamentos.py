print('BEM VINDO AO GERENCIADOR DE PAGAMENTOS!')

valor = float(input('Digite o valor do produto: R$'))

print('''Escolha a condição de pagamento:
[1] À vista dinheiro/cheque
[2] À vista cartão
[3] Cartão em 2x
[4] Cartão em 3x ou mais''')

condicao_de_pagamento = int(input('Digite a condição de pagamento: '))

if condicao_de_pagamento == 1:
    print('O valor do pagamento à vista é de R$ {:.2f}'.format(valor - (valor * 0.10)))

elif condicao_de_pagamento == 2:
    print('O valor do pagamento à vista no cartão é de R$ {:.2f}'.format(valor - (valor * 0.05)))

elif condicao_de_pagamento == 3:
    print('O valor do pagamento no cartão em 2x é de R$ {:.2f}'.format(valor))

elif condicao_de_pagamento == 4:
    print('O valor do pagamento no cartão em 3x ou mais é de R$ {:.2f}'.format(valor + (valor * 0.20)))

else:
    print('Opção de pagamento inválida, tente novamente!')


