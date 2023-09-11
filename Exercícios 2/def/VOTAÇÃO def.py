def vota(ano):
    from datetime import datetime
    ano_atual = datetime.today().year
    idade = ano_atual - ano
    if idade < 16:
        return f'{idade} anos: NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'{idade} anos: VOTO OPCIONAL'
    else:
        return f'{idade} anos: VOTO OBRIGATÓRIO'


nascimento = int(input('Digite o seu ano de nascimento: '))
print(vota(nascimento))
