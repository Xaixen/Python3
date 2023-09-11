
while True: # O laço repete para sempre
    nome = str(input('Digite um nome [FIM] para encerrar: ')).upper()
    print(nome)
    if nome in ['FIM','F']:
        break # operador para parar o laço

