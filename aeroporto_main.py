from escolhas import *
from CheckIn import *

cidade_origem = ["recife", "garanhuns", "maceio", "natal"]
cidade_destino = cidade_origem.copy()

ver_cidade(cidade_origem)
origem_cidade = escolher_origem(cidade_origem, cidade_destino)

print("")

ver_cidade(cidade_destino)
destino_cidade = escolher_destino(cidade_destino)

print(f'\nVoce escolhe {destino_cidade} como sua cidade de chegada')
print(f'\nVoce escolhe {origem_cidade} como sua cidade de partida')

passageiros = Passageiros()

passageiros.adicionar('adson')
passageiros.adicionar('alexandre')
passageiros.adicionar('amanda')
passageiros.adicionar('elen')

print(passageiros.Lista_nome_passageiros)
passageiros.deletar()

print(passageiros.Lista_nome_passageiros)