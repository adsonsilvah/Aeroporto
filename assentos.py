import numpy as np

classePrimeira = np.array([["1","2"],["3","4"]])

classeEco = np.matrix([["1","2"],["3","4"]])

classe = input("escolha a classe: ")

if classe == "primeira":
    print(classePrimeira)
    assento = input("escolha o assento: ")
    nome = input("coloque seu nome: ")
    for i in range(len(classePrimeira)):
        for j in range(len(classePrimeira[i])):
            if classePrimeira[i][j] == assento :
                classePrimeira[i][j] = nome

for linha in classePrimeira:
    print(" ".join(map(str, linha)))
print(classePrimeira)
