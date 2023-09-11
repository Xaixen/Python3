from exercicios.uteis.textos import titulo


def encontrar(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Arquivo não criado')
    else:
        print(f'Arquivo {nome} criado com sucesso')


def ler(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Não foi possivel ler o arquivo')
    else:
        titulo('CADASTRO DE PESSOAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<15}{dado[1]} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconheciso', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um problema ao escrever o arquivo')
        else:
            print(f'{nome} cadastrado com sucesso!')
