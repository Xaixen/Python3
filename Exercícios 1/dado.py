from random import randint
import time

print('-=' * 10)
print(' ' * 2, '\33[7;30;46m[DADO VIRTUAL]\33[m')
print('-=' * 10)
dado = randint(1, 6)
botao = str(input('Aperte \33[36mEnter\33[m para começar'))
if botao == '':
    print('\33[36mGenerate...\33[m')
    time.sleep(randint(1, 3))
    print(dado)
