frase = str(input("digite uma frase: ")).upper().strip()
print("A letra A aparece {}  vezes na frase ".format(frase.count("A")))
print("A primeira letra A apareceu na posição {}".format(frase.find("A")))
print("A ultima letra A aparece na posição {}".format(frase.rfind("A")))