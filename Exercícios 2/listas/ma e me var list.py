maior = menor = 0
lista = ['']
for c in range(1, 6):
    lista.append(int(input(f'Digite o {c}° número: ')))
    if c == 1:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
lista.remove('')
print('--' * 10)
print(f'Os valores digitados na lista: {lista}')
print(f'o maior valor é {maior} na posição', end='')
for p, n in enumerate(lista):
    if n == maior:
        print(f' {p}...', end='')
print(f'\nO menor valor é {menor} na posição', end='')
for p, n in enumerate(lista):
    if n == menor:
        print(f' {p}...', end='')