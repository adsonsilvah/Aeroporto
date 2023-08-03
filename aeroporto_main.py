from escolhas import ver_cidade
from escolhas import escolher_destino
from escolhas import escolher_origem
#cidade_origem = ["recife", "garanhuns", "são paulo", "teresina"]
# cidade_destino = cidade_origem.copy()

# for cidade in cidade_origem:
#      print(f"{cidade}")
#  origem = input("selecione sua cidadede origem ")

# cidade_destino.remove(origem)

# for cidade in cidade_destino:
#     print(f"{cidade}")
# destino = input("selecione sua cidadede destino ")

# def ver_cidade(lista_cidades):
#     for cidade in lista_cidades:
#         print(f"{cidade}")

# def escolher_origem(lista_origem, lista_chegada):
#      while True: 
#         origem = input("Selecione sua cidade de origem: ")
#         if origem in lista_origem:
#             lista_chegada.remove(origem)
#             return origem
#         else:
#             print(f"cidade {origem} não esta na lista de voos, essa e a lista de nossos voos: \n")
#             ver_cidade(lista_origem)
         

# def escolher_destino(lista_chegada):
#     while True:
#         destino = input("Selecione sua cidade de destino: ")
#         if destino in lista_chegada:
#             return destino
#         else:
#             print(f"cidade {destino} não esta na lista de voos, essa e a lista de nossos voos: \n")
#             ver_cidade(lista_chegada)

cidade_origem = ["recife", "garanhuns", "são paulo", "teresina"]
cidade_destino = cidade_origem.copy()

ver_cidade(cidade_origem)
origem_cidade = escolher_origem(cidade_origem, cidade_destino)

print("")

ver_cidade(cidade_destino)
destino_cidade = escolher_destino(cidade_destino)

print(f'\nVoce escolhe {destino_cidade} como sua cidade de chegada')
print(f'\nVoce escolhe {origem_cidade} como sua cidade de partida')

