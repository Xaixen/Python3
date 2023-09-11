s = float(input('digite seu salário :R$ '))
if s <= 1250:
    s = s * 1.15
    a = s * 0.15
    print('Seu salário teve um acrésimo de 15% \n'
          'Valor total de R${}'.format(s))
else:
    s = s * 1.10
    print('seu salário teve um acrésimo de 10% \n'
          'valor total de R${}'.format(s))
