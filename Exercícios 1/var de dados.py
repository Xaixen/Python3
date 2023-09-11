sex = 1
while sex != 'M' and sex != 'F':
    sex = str(input('digite o sexo [M ou F]: ')).upper()
    if sex not in 'MF':
        print('Dados inválidos, tente novamente!')
print(f'Sexo {sex} registrado com Sucesso.')