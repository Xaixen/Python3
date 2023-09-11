lista = ('Lápis', 1.75,
         'Borracha', 2,
         'Caderno', 10,
         'Estojo', 4.50,
         'régua', 2.24,
         'Canetinhas', 14.90,
         'Mochila', 120.01,
         'Livro', 55.60,
         'Cola de isopor', 12,
         'Lancheira Premium', 93.99)
print('==' * 20)
print(f'{"LISTA DE PREÇOS":^40}')
print('==' * 20)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}',end='')
    else:
        print(f'{"R$"}{lista[c]:.2f}')
print(f'{"FIM DO PROGRAMA":=^40}')