import datetime
ano = int(input('digite o ano para análisar ou 0 para o ano atual: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0:
    print('\33[32m ano {} é Bissexto.'.format(ano))
else:
    print('O ano {}\33[31m não é bissexto. '.format(ano))