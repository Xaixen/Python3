def ANSI(estilo=7, txt=0, marca=0):
    '''
    Código ANSI
    \33[style;text;backm
    Style
    0 normal    1 negrito	4 sublinhado    7 negativo
    Text
    30 branco   31 vermelho     32 verde	33 amarelho
    34 azul	    35 roxo	        36 ciano	37 cinza
    Back
    40 branco   41 vermelho     42 verde	43 amarelho
    34 azul     45 roxo	        46 ciano	47 cinza

    :param estilo: Estilo da Fonte
    :param txt: Cor do texto
    :param marca: Cor do marcação(marca texto)
    :return: retorna o codigo ANSI com as cores definidas.
    '''
    cores = f'\33[{estilo};{txt};{marca}m'
    return cores


def cores(txt='teste', cor=3, sub=False):
    '''
    CORES DEFINIDAS:
    0 branco   1 vermelho     2 verde	3 amarelho
    4 azul	   5 roxo	      6 ciano   7 cinza
    8 Neutro
    ______________________________________________
    :param txt: Escreve o texto desejado
    :param cor: Escolha uma cor de 0 a 8, cada número representa uma cor
    :param sub: padrao falso, para sublinhar o texto basta digitar sub=True
    :return: retorna o texo com a cor desejada
    '''
    if sub:
        fonte = '4'
    else:
        fonte = '1'
    c = (
         f'\33[{fonte};30m',
         f'\33[{fonte};31m',
         f'\33[{fonte};32m',
         f'\33[{fonte};33m',
         f'\33[{fonte};34m',
         f'\33[{fonte};35m',
         f'\33[{fonte};36m',
         f'\33[{fonte};37m',
         f'\33[m')

    return f'{c[cor]}{txt}{c[8]}'

