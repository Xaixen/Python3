
a = int(input('1° valor: '))
b = int(input('2° valor: '))
c = int(input('3° valor: '))
# verificando o menor
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando o maior
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor foi {}.\n'
      'o maior valor foi {}'.format(menor, maior))
