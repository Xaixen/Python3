from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(1, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual é a sua jogada? = '))
print('PEDRA!')
sleep(0.5)
print('PAPEL!')
sleep(0.5)
print('TESOOOURA!')
sleep(1)
print('-=' * 10)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[player]))
print('-=' * 10)
if pc == 0:
    if player == 0:
        print('EMPATE')
    elif player == 1:
        print('Você Venceu')
    elif player == 2:
        print('Você Perdeu')
elif pc == 1:
    if player == 0:
        print('Você Perdeu')
    elif player == 1:
        print('EMPATE')
    elif player == 2:
        print('Você Venceu')
elif pc == 2:
    if player == 0:
        print('Você Venceu')
    elif player == 1:
        print('Você Perdeu')
    elif player == 2:
        print('EMPATE')