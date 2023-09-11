try:  # tente
    'operação'
    n = int(input('numero A: '))
    n2 = int(input('numero B: '))
    r = n / n2
except (ValueError, TypeError):
    print('O usuario escreveu algo de errado')
except ZeroDivisionError:
    print('Não e possível dividir o zero.')
except KeyboardInterrupt:
    print('O usuario não respondeu todos os dados')
except Exception as erro:  # exeto
    'falha caso de falha oque aparecer'
    print(f'Algo deu errado', erro.__class__)

else:  # senao
    'deu certo'
    print('Respota', r)

finally:  # final
    'deu certo ou falha'
    print('Volte sempre')
