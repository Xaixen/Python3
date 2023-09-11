d = float(input('digite a distancia da viagem desejada:'))
print('=='* 20)
preço = d * 0.50 if d <= 200 else d * 0.45
print('O valor cobrado será de {:.2f}'.format(preço))
print('=='* 20)