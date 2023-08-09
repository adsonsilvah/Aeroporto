from escolhas import *
from CheckIn import *
from checkout import *
#parte escolha das cidades
cidade_origem = ["recife", "garanhuns", "maceio", "natal"]
#inicializadores 
escolhas = escolhas(cidade_origem)
checkin = checkin()


print("\nCidades de Origem:\n")
escolhas.ver_cidade(escolhas.lista_origem)
origem_cidade = escolhas.escolher_origem()

print("\nCidades de Destino:\n")
escolhas.ver_cidade(escolhas.lista_chegada)
destino_cidade = escolhas.escolher_destino()

print(f'Você escolheu {origem_cidade} como sua cidade de partida.\n')
print(f'\nVocê escolheu {destino_cidade} como sua cidade de chegada.\n')


#fila do checkin
#checkin.adicionar('adson')
#checkin.adicionar('alexandre')
# checkin.adicionar('amanda')
# checkin.adicionar('elen')
# checkin.adicionar('eraylson')
while True:
    nome = input('nome passageiro: ')
    if nome == "sair":
        break
    else:
        checkin.adicionar(nome)
Lista_nome_passageiros_saida = checkin.Lista_nome_passageiros
print(checkin.Lista_nome_passageiros)

checkin.deletar()
# checkin.deletar()
# checkin.deletar()
# checkin.deletar()
# checkin.deletar()

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