s1 = int(input('digite o 1° segmento: '))
s2 = int(input('digite o 2° segmento: '))
s3 = int(input('digite o 3° segmento: '))
if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima podem fomar um triangulo: ', end='')
    if s1 == s2 == s3 == s1:
        print('\33[33mEQUILÁTERO\33[m')
    elif s1 != s2 != s3 != s1:
        print('\33[31mESCALENO\33[m')
    else:
        print('\33[36mISÓCELES\33[m')
else:
    print('Os segmentos \33[31mNÃO\33[m podem formar um triangulo')
