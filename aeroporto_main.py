from escolhas import *
from CheckIn import *
from checkout import *

checkin = checkin()

print()
print("Bem vindo(a) ao 321Quilometros")
print()

cidades = ["Recife", "Garanhuns", "Maceio", "Natal"]
escolhas = Escolhas(cidades)
origem = escolhas.escolher_origem()
print(f"Origem selecionada: {origem}")
destino = escolhas.escolher_destino()
print(f"Destino selecionado: {destino}")


print()


print("Escolha a empresa aerea e compre sua passagem:")


empresas_aereas = ["Azul", "GOL", "Latam"]

#valores_passagens = {
 #   "Azul": {"Recife": 300, "Natal": 400, "Garanhuns": 350},
#   "GOL": {"Recife": 320, "Natal": 410, "Garanhuns": 360},
#    "Latam": {"Recife": 310, "Natal": 390, "Garanhuns": 340},
#}

Azul = {"Recife": 300, "Natal": 400, "Garanhuns": 350, "Maceio" : 500}
Gol = {"Recife": 320, "Natal": 410, "Garanhuns": 360, "Maceio": 510}
Latam = {"Recife": 310, "Natal": 390, "Garanhuns": 340, "Maceio": 480}


aeroportos = cidades

destino_escolhido = destino

chave_selecionada = destino_escolhido

passagens = [("Azul", Azul[destino_escolhido]), ("GOL", Gol[destino_escolhido]), 
             ("Latam", Latam[destino_escolhido])]

def bubble_sort(passagens):
    tamanho_passagens = len(passagens)
    for i in range(tamanho_passagens):
        for j in range(0, tamanho_passagens - i - 1):
            if passagens[j][1] > passagens[j + 1][1]:
                passagens[j], passagens[j + 1] = passagens[j + 1], passagens[j]

bubble_sort(passagens)

print("Empresas disponíveis para o destino", destino_escolhido, ":")
for empresa in empresas_aereas:
    print(empresa)

print("Passagens ordenadas por preço:")
for empresa, preco in passagens:
    print(f"{empresa}: R${preco:.2f}")

empresa_escolhida = input("Escolha uma empresa aérea: ")

preco_escolhido = None

for empresa, preco in passagens:
    if empresa == empresa_escolhida:
        preco_escolhido = preco
        break

if preco_escolhido is not None:
    print(f"Você escolheu a empresa aérea: {empresa_escolhida}")
    print(f"O valor da passagem para {destino_escolhido} é R${preco_escolhido:.2f}")
else:
    print("Empresa não encontrada")

print(f'Você escolheu {origem} como sua cidade de partida.\n')
print(f'Você escolheu {destino} como sua cidade de chegada.\n')



while True:
    nome = input('nome passageiro: ')
    if nome == "sair":
        break
    else:
        checkin.adicionar(nome)
Lista_nome_passageiros_saida = checkin.Lista_nome_passageiros
print(checkin.Lista_nome_passageiros)

checkin.deletar()

print(checkin.Lista_nome_passageiros)

#pilha checkout
checkout = checkout(Lista_nome_passageiros_saida)
print(f"tem: {checkout.size()} passageiros dentro do avião")

while checkout.size() > 0:
    print(f"O primeiro passageiro a desembarcar do avião: {checkout.head()}")
    passageiro = checkout.desempilhar()
    print(f"O passageiro, {passageiro} saiu do avião")
    print(f"Faltam: {checkout.size()} passageiros saírem do avião\n")

print("Todos os passageiros saíram do avião.")