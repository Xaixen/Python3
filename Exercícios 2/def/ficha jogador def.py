def ficha(nome='desconecido', gol=0):
    print(f'O jogador {nome} fez {gol} gol(s).')


nome = input("Digite o nome do jogador: ").capitalize().strip()
gols = input(f"Quantos gols {nome} fez? ")
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol=0)
else:
    ficha(nome, gols)