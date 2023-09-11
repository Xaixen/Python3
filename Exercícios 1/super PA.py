primeiro = int(input('Primeiro termo: '))
razao = int(input('razão PA: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(termo, '¬ ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Deseja ver quantos termos a mais?'))
print(f'Progressão finalizada com {total} termos mostrados.')