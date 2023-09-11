def metade(valor, real=True):
    metade = valor / 2
    formato = conversão(metade)
    return metade if real is False else formato


def dobro(valor, real=True):
    dobro = valor * 2
    formato = conversão(dobro)
    return dobro if not real else formato


def acrescimo(valor, porcentagem, real=True):
    acrescimo = valor + valor / 100 * porcentagem
    formato = conversão(acrescimo)
    return acrescimo if not real else formato


def desconto(valor, porcentagem, real=True):
    desconto = valor - valor / 100 * porcentagem
    formato = conversão(desconto)
    return desconto if not real else formato


def resumo(valor, aumento=10, abaixo=10):
    print('--' * 20)
    print(f'{"RESUMO DO VALOR":^40}')
    print('--' * 20)
    print(f'Preço analisado...\t\t{conversão(valor)}\n'
          f'Dobro do preço...\t\t{dobro(valor)}\n'
          f'Metade do preço...\t\t{metade(valor)}\n'
          f'Acréscimo de {aumento}%...\t\t{acrescimo(valor, aumento)}\n'
          f'Desconto de {abaixo}%...\t\t{desconto(valor, abaixo)}')
    print('--' * 20)


def conversão(valor):
    formato = f'R${valor:,.2f}'.replace('.', ' ').replace(',', '.').replace(' ', ',')
    return formato

