total = 0
import random
while True:
    print('~~' * 12)
    print(' ' * 5, 'PAR OU IMPAR')
    print('~~' * 12)
    pc = random.randint(1, 10)
    pi = 'h'
    while pi not in 'PI':
        pi = str(input('Par ou Impar:[P/I] ')).upper().strip()[0]
    n = int(input('Digite um número: '))
    soma = n + pc
    print('__' * 12)
    print(f'Você jogou {n} e o computador {pc}')
    if soma % 2 == 0:
        nf = 'PAR'
    elif not soma % 2 == 0:
        nf = 'IMPAR'
    print(f'A soma deu {soma}, valor deu {nf}')
    if pi in 'P' and nf == 'PAR':
        print('Você VENCEU')
        total += 1
    elif pi in 'I' and nf == 'IMPAR':
        print('Você VENCEU')
        total += 1
    else:
        print('Você PERDEU')
        break
print('______O JOGO ACABOU______')
print('')
print('   RANKING PAR OU IMPAR ')
print('__' * 15)
print(f'''Vitórias Consecutivas = {total}
mais de 10 vitórias = Uma Máquina
8 até 10 vitorias = Aulas
4 a 7 vitórias = bom
1 a 3 vitórias = Normal
0 vitória = Não teve infância''')