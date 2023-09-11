from random import randint
sorte = [randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10)]
def print_especial(txt):
    print(f'~' * len(txt))
    print(txt)
    print(f'~' * len(txt))

def sortear():
    print(f'{"SORTEANDO OS 5 VALORES...":-^40}')
    for n in sorte:
        print(n, end=' ')
    print('PRONTO!')

def soma_sorte():
    soma = 0
    for num in sorte:
        if num % 2 == 0:
            soma += num
    print(f'A soma dos valores {sorte} pares: {soma}')


sortear()
soma_sorte()