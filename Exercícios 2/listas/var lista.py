
lista = []
while True:
    print('=-' * 11)
    print('PARA PARA APERTE "111'
          '"')
    n = int(input('Digite um número:'))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado...')
    else:
        print('O valor não pode ser duplicado!')
    if n == 111:
        break
lista.remove(111)
print('=-' * 11)
print(f'lista Concluida = {sorted(lista)}')