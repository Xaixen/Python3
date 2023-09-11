lista = ([], [])

for c in range(1, 8):
    n = int(input(f'digite o {c}° numero:'))
    if n % 2 == 0:
      lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(lista)
print(lista[0])
print(lista[1])
