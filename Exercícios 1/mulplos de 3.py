cont = 0
soma = 0
for n3 in range(1, 501, 2):
    if n3 % 3 == 0:
        cont = cont + 1
        soma = soma + n3
print('A soma total entre os {} valores são de {}'.format(cont, soma))

