#Boletim [Listas]
ficha = list()
while True:
    nome = str(input('Nome:'))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    reps = str(input('Deseja continuar?[S/N]')).strip().upper()[0]
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    if reps in 'N':
        break
print('♦' * 20)
print(f'{"N°":<4}{"NOME":<10}{"MEDIA":>0}')
print('♦' * 20)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>0.1f}')
while True:
    op = int(input('Mostrar notas de qual aluno? [999 PARA SAIR]: '))
    if op == 999:
        print('finalizando...')
        break
    if op <= len(ficha) - 1:
        print(f'NOtas de {ficha[op][0]} são {ficha[op][1]}')
print(F'{" BOAS FÉRIAS ":=^40}')