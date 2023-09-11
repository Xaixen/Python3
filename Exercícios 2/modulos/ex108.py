from exercicios.uteis.moeda import moeda

n = float(input('Digite O valor: R$'))
print(f'A metade de R${n} é R$', moeda.metade(n))
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'O valor do acréscimo de 10 % é R${moeda.acrescimo(n, 10)}')
