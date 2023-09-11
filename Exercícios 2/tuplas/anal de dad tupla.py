n = (int(input('Digite o 1° número: ')),
    int(input('Digite o 2° número: ')),
    int(input('digite o 3° número: ')),
     int(input('Digite o 4° número: ')))

print(f' os valores digitados:{n}')
print(f'o valor 9 apareceu {n.count(9)} vez(es).')
if 3 in n:
    print(f'O 3 esta na {n.index(3)+1}° posição.')
else:
    print('O valor 3 não foi digitado.')
print(f'Os valores pares são ', end='')
for c in n:
    if c % 2 == 0:
        print(c, end=', ')