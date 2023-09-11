# galera = [['Joao', 19], ['Ana', 15], ['maminha', 26], ['Maria', 23], ['Nadjarah', 22]]
# print(galera[1])

galera = []
dados = []
totm = totn = 0
for c in range(1,4):
    print(f'{"PESSOA":->15} {c:-<10}')
    dados.append(str(input('Digite um nome: ')).capitalize())
    dados.append(int(input('Digite um número: ')))
    galera.append(dados[:]) #[:] <- Copiar os dados da lista
    dados.clear()
print('-' * 30)
print(galera)

for p in galera:
    if p[1] <= 18:
        totm += 1
        print(f'{p[0]} é maior de idade\n')
    else:
        totn += 1
        print(f'{p[0]} é menor de idade:\n')

print(f'O Total de maior de idade: {totm}\n'
      f'TOtal de Menore de idade: {totn}')
