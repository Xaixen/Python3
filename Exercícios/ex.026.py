from random import randint
from time import sleep
pc = randint(0, 3)
print('==' * 25)
print('De 0 a 3 em que número o computador está pensando?')
print('==' * 25)
u = int(input('digite o número: '))
print()
print('PROCESSANDO...')
sleep(1)
if pc == u:
    print('Você acertou parábens!')
else:
    print('O número escolhido foi {} tente outra vez!'.format(pc))
