import random
lista = list()
jogos = list()
print('••' * 20)
print(f'{"MEGA SENA":^40}')
print('••' * 20)
rep = int(input('quanto jogos quer sortear? '))
tot = 1
while tot <= rep:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f'{f"SORTEANDO {rep} JOGOS":•^40}')
for i, j in enumerate(jogos):
    print(f'JOGO{i+1}: {j}')