'''leia o nome idade e sexo de 4 pessoas.No final mostre: a média de idade do grupo
qual é o nome do homem mais velho
quantas mulheres têm menos de 20 anos.'''
# variaveis contadoras
somai = 0
maiorm = 0
fmi = 0
# Informações de 4 pessoas
for n in range(1,5):
    print('___________{} PESSOA ____________'.format(n))
    nome = str(input('digite seu nome: '))
    i = int(input('Qual é sua idade?: '))
    sex = str(input('Sexo [M/F]: ')).upper()
    # Calculando a média de idade
    somai += i
    mediai = somai / 4
    # Identificando o nome do homem mais velho
    if i > maiorm and sex in 'Mm':
        maiorm = i
        nomem = nome
    # Identificando quantas mulheres tem menos que 20 anos
    if sex in 'Ff' and 20 < i:
        fmi += 1
# Resultado
print('A média da idade do grupo são de {} anos'.format(mediai))
print('O homem mais velho tem {} anos e se chama {}'.format(maiorm, nomem))
print('{} mulher(es) tem a idade abaixo que 20 anos'.format(fmi))
