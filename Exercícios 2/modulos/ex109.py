from exercicios.uteis import moeda

n = float(input('Digite O valor: R$'))
print(f'A metade de R${n} é {moeda.metade(n)}')
print(f'O dobrode R${n} é {moeda.dobro(n)}')
print(f'O valor do acrésimo de 10 % é {moeda.acrescimo(n, 10)}')
print(f'O valor descontado 20% é {moeda.desconto(n, 20)}')

