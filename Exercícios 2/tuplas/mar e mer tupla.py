import random
sorte = (random.randint(1, 10), random.randint(1, 10), random.randint(1, 10), random.randint(1, 10))
print('Os números sorteados: ',end='')
for n in sorte:
    print(f'{n}',end=' ')
print(f'\nO número maior sorteado é {max(sorte)}')
print(f'O número menor sorteado é {min(sorte)}')
