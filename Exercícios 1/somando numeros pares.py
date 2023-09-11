cont = 0
soma = 0
for c in range(1, 7):
    n = int(input('Digite o {}° número: '.format(c)))
    if n % 2 == 0:
        cont += 1
        soma += n
print('Os {} valores pares, somados são {}'.format(cont, soma))
