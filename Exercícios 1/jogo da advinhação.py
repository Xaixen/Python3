from random import randint
from time import sleep
print("~~" * 20)
print('JOGO DA ADVINHAÇÃO')
print("~~" * 20)
pc = randint(1, 10)
print('''Olá sou o computador...
Acabei de pensar em um número de 1 a 10
Será que você é capaz de advinhar ?''')
tentar = 0
pal = 0
while pal != pc:
    pal = int(input('Digite o seu palpite: '))
    tentar += 1
    if pal < pc:
        print('Mais... Tente outra vez!')
    elif pal > pc:
        print('Menos... Tente outra vez!')
print(f'Você conseguiu em {tentar} tentativas parabéns!')
sleep(2)
print("=-" * 20)
print('''RANKING DE TENTATIVAS

1 tentativa = Prof. Xavier
2 tentativas = Profisional
3 a 4 tentativas = Bom
5 a 7 tentativas = Normal 
Acima de 7 tentativas = Noob''')