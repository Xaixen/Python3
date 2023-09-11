matriz = ([0,0,0], [0,0,0], [0,0,0])
spar = somac = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite a matriz na posição {[l],[c]}:'))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print(f'A soma dos valores pares são:{spar}')
for l in range(0, 3):
    somac += matriz[l][2]
print(f'A soma da ultima coluna é: {somac}')
for c in range(0, 3):
    if c == 0:
        maior += matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]
print(f'O maior na 1° linha: {maior}')