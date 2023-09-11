# lista = []
# for cont in range(1, 4):
#     lista.append(input(f'Digite o {cont}° numero:'))
#
# for c, v in enumerate(lista):
#     print(f'na posição {c} encontrei o valor {v}')

# enumerate pega o valor e a chave

lista = [2, 4, 6, 8]
listb = lista[:]  # cria uma copia de A dentro de B
listb[2] = 8
print(f'lista A:{lista} '
      f'lista B:{listb}')
