from exercicios.uteis import moeda, cores
cor = cores.ANSI(1, 30, 47)
n = float(input(f'{cor}Digite O valor: R$'))
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobrode R${n} é R${moeda.dobro(n)}')
print(f'O valor do acrésimo de 10 % é R${moeda.acrescimo(n, 10)}')
