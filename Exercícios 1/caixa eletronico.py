
print('==' * 15)
print('{:^30}'.format('XABLAU BANK'))
print('==' * 15)
v = int(input('Quanto você quer sacar? R$'))
print('==' * 15)
ced = 50
totced = 0
while True:
    if v >= ced:
        v -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'O total de {totced} cedulás de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if v == 0:
            break
print('==' * 15)
print('Tenha um otimo dia, XABLAU BANK')


