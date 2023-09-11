import datetime
atual = datetime.date.today().year

a = int(input('Digite seu ano de nascimento: '))
idade = 2023 - a
print('Você tem {} anos em {}'.format(idade, atual))
if idade == 18:
    print('Você deve se alistar imediatamente!\n'
          'Acesse o link:www.alistamentoolline.com')
elif idade < 18:
    c = 18 - idade
    c2 = atual + c
    print('Faltam {} anos.\n'
          'Seu alistamento será em {}.'.format(c, c2))
else:
    c = idade - 18
    c2 = atual - c
    print('Você deveria ter se alistado há {} ano(s) atrás\n'
          'Seu alistamento aconteceu em {}'. format(c, c2))
