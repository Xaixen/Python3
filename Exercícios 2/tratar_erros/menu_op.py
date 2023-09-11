from exercicios.uteis import textos
from exercicios.uteis import erros
from exercicios.uteis import arquivos
from time import sleep
arq = 'cadastro'
if not arquivos.encontrar(arq):
    arquivos.criar(arq)
while True:
    textos.menu(['Ver pessoas cadastradas','Cadastrar nova pessoas','sair do programa'])
    opc = erros.leiaint('Escolha uma Opção: ')
    if opc == 1:
        arquivos.ler(arq)
        sleep(2)
    elif opc == 2:
        textos.titulo('CADASTRAR PESSOAS')
        nome = input('Nome:')
        idade = erros.leiaint('Idade: ')
        arquivos.cadastrar(arq, nome, idade)
        sleep(2)
    elif opc == 3:
        print('Saindo do programa...')
        sleep(2)
        break
    else:
        print('Opção invalida')
