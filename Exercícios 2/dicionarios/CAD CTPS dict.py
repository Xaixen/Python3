from datetime import datetime
cadastro = {}

cadastro['nome'] = input('Digite o seu nome: ').capitalize()
Ano_nasci = int(input('ano de nascimento: '))
cadastro['idade'] = datetime.now().year - Ano_nasci
cadastro['CTPS'] = int(input('Nº da carteira de trabalho (0 = não possui): '))
if cadastro['CTPS'] != 0:
    cadastro['Ano contratado'] = int(input('Ano que foi contratado: '))
    cadastro['salario'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['idade'] + (cadastro['Ano contratado'] + 35) - datetime.now().year
print('-='*21)
print('Informações cadastradas')
for c, v in cadastro.items():
    print(f'{c}: {v}')