def ver_cidade(lista_cidades):
    for cidade in lista_cidades:
        print(f"{cidade}")

def escolher_origem(lista_origem, lista_chegada):
     while True: 
        origem = input("Selecione sua cidade de origem: ")
        if origem in lista_origem:
            lista_chegada.remove(origem)
            return origem
        else:
            print(f"cidade {origem} não esta na lista de voos, essa e a lista de nossos voos: \n")
            ver_cidade(lista_origem)
         

def escolher_destino(lista_chegada):
    while True:
        destino = input("Selecione sua cidade de destino: ")
        if destino in lista_chegada:
            return destino
        else:
            print(f"cidade {destino} não esta na lista de voos, essa e a lista de nossos voos: \n")
            ver_cidade(lista_chegada)