from datetime import date

ano = int(input('digite o seu ano de nascimento: '))
idade = date.today().year - ano
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('classsificação: MIRIM')
elif idade <= 14:
    print('CLassificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')
