b1 = float(input('digite sua nota no 1° bimestre: '))
b2 = float(input('digite sua nota no 2° bimestre: '))
b3 = float(input('digite sua nota no 3° bimestre: '))
b4 = float(input('digite sua nota no 4° bimestre: '))
soma = (b1 + b2 + b3 + b4) / 4
print('A media total do aluno foi = {:.1f}'.format(soma))
if soma >= 7:
    print('Aluno \33[32mAPROVADO\33[M')
elif soma < 7 and soma >= 5:
    print('Aluno de RECUPERAÇÃO')
else:
    print('Aluno REPROVADO\n tente se esforçar mais no próximo ano!' )