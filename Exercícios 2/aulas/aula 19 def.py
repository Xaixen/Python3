def area(l1, l2):
    quadadro= l1 * l2
    print(f'o valor da área {l1}x{l2} = {quadadro}m²')
def linha(txt):
    print('_='* 20)
    print(txt)
    print('_='* 20)


linha('CACULAR ÁREA')
base = float(input('Digite a bese da área: '))
altura =  float(input('Digite a altura da área: '))
area(base, altura)
