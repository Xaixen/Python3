#IMPORTANDO PACKS
from random import randint
from operator import itemgetter
from time import sleep

#CRIANDO UM DICIONARIO
dicionario = {'Jogador1': randint(1, 10), 'Jogador2': randint(1, 10), 'Jogador3': randint(1, 10), 'Jogador4': randint(1, 10)}

#IMPRIMINDO O DICIONARIO COM OS NUMEROS SORTEADOS
for jogador, dados in dicionario.items():
    print(f'{jogador} tirou {dados}')

#ORDENANDO OS JOGARDORES POR MAIORES NUMEROS
print(F'{"RANK DE JOGADORES":-^40}')
rank = sorted(dicionario.items(),key=itemgetter(1), reverse=True)
for i, j in enumerate(rank):
    print(f'{i}ºlugar: {j[0]} -> {j[1]}')
    sleep(1)