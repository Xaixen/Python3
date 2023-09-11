pilha = []
ex = str(input('Digite a expressão: '))
for sim in ex:
    if sim == '(':
        pilha.append('(')
    elif sim == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão Válida')
else:
    print('\33[31mExpressão Inválida')