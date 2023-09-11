primeiro = int(input('Primeiro termo: '))
razao = int(input('razão PA: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, '¬ ', end='')
    termo += razao
    cont += 1
print('FIM')
