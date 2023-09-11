tot = 0
n = int(input('Escolha um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\33[33m', end='')
        tot += 1
    else:
        print('\33[m', end='')
    print(c,end=' ')
print('\n\33[mO número {} foi divisível {} vezes'.format(n, tot))
if tot == 2:
    print('Por isso, É PRIMO')
else:
    print('Número {} NÃO é primo.'.format(n))