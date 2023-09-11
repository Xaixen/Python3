import
print(f'{"FÉRIAS DE JULHO":-^40}')
dicionario = dict()
dicionario['nome'] = input('Digite um nome: ').capitalize()
dicionario['média'] = float(input(f'A média de {dicionario["nome"]} foi: '))
print(dicionario)
dicionario['situação'] = 'aluno aprovado, BOAS FÉRIAS!' if dicionario['média'] >= 7 else'Aluno de recuperação'
print('SITUAÇÃO:', dicionario['situação'])
