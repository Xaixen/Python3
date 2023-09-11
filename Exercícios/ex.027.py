v = int(input('digite sua velocidade atual do carro:'))
if v > 80:
    c = (v - 80) * 7
    print('MULTADO! Você excedeu o limite permitido de 80km/h')
    print('voce deve pagar a multa de R${}'.format(c))
print('Tenha um ótimo dia! Dirija com segurança!')


