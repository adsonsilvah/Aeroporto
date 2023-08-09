class escolhas:
    def __init__(self, lista_origem):
        self.lista_origem = lista_origem
        self.lista_chegada = lista_origem.copy()

    def ver_cidade(self, lista_cidades):
        for cidade in lista_cidades:
            print(f"{cidade}")

    def escolher_origem(self):
        while True:
            origem = input("Selecione sua cidade de origem: ")
            if origem in self.lista_origem:
                self.lista_chegada.remove(origem)
                return origem
            else:
                print(f"Cidade {origem} não está na lista de voos. Esta é a lista de nossos voos:")
                self.ver_cidade(self.lista_origem)

    def escolher_destino(self):
        while True:
            destino = input("Selecione sua cidade de destino: ")
            if destino in self.lista_chegada:
                return destino
            else:
                print(f"Cidade {destino} não está na lista de voos. Esta é a lista de nossos voos:")
                self.ver_cidade(self.lista_chegada)