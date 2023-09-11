# tuplas
fruta = ('banana', 'melão', 'laranja', 'melancia', 'uvas', 'limão')
a = (1,6,4,0)
b = ('marquin',20,6.80)
c = a + b
print(fruta[0], '\n')

for comida in fruta:
    print(f'{comida[0]} ')
print('Acabou \n')

for c in range(0, len(fruta)):
    print(fruta[c:6])
print('')
print(a, b, c)
