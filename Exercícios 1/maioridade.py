totm = 0
totn = 0
from datetime import date
for c in range(1, 7 + 1):
    ano = int(input('digite o ano de nacimento da {}° pessoa: '.format(c)))
    idade = date.today().year - ano
    if idade >= 18:
        totm += 1
    else:
        totn += 1
print('Maiores de idade são {} \n'
      'Menores de idade são {}'.format(totm, totn))