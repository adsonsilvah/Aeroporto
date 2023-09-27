class Escolhas:
    def __init__(self, lista_origem):
        self.lista_origem = lista_origem
        self.lista_chegada = lista_origem.copy()

    def ver_cidade(self, lista_cidades):
        for cidade in lista_cidades:
            print(f"{cidade}")

    def escolher_origem(self):
        busca_origem = BuscaBinaria(self.lista_origem)

        while True:
            origem = input("Selecione sua cidade de origem: ")
            if busca_origem.buscar(origem) is not None:
                self.lista_chegada.remove(origem)
                return origem
            else:
                print(f"Cidade {origem} não está na lista de voos. Esta é a lista de nossos voos:")
                lista_ordenada = QuickSort(self.lista_origem)
                lista_ordenada.sort()
                self.ver_cidade(lista_ordenada.lista)

    def escolher_destino(self):
        busca_destino = BuscaBinaria(self.lista_chegada)

        while True:
            destino = input("Selecione sua cidade de destino: ")
            if busca_destino.buscar(destino) is not None: 
                return destino
            else:
                print(f"Cidade {destino} não está na lista de voos. Esta é a lista de nossos voos:")
                lista_ordenada = QuickSort(self.lista_chegada)
                lista_ordenada.sort()
                self.ver_cidade(lista_ordenada.lista)

class QuickSort:
    def __init__(self, lista):
        self.lista = lista

    def sort(self, inicio=0, fim=None):
        if fim is None:
            fim = len(self.lista) - 1

        if inicio < fim:
            # Particionar
            divisor = self.particionar(inicio, fim)
            self.sort(inicio, divisor - 1)
            self.sort(divisor + 1, fim)

    def particionar(self, inicio, fim):
        pivot = self.lista[fim]
        divisor = inicio
        for i in range(inicio, fim):
            if self.lista[i] < pivot:
                self.lista[divisor], self.lista[i] = self.lista[i], self.lista[divisor]
                divisor += 1

        self.lista[divisor], self.lista[fim] = self.lista[fim], self.lista[divisor]
        return divisor

class BuscaBinaria:
    def __init__(self, lista_busca):
        self.lista_busca = lista_busca
        self.quick_sort = QuickSort(lista_busca) 

    def buscar(self, alvo):
        self.quick_sort.sort()  
        lista_ordenada = self.quick_sort.lista

        esquerda, direita = 0, len(lista_ordenada) - 1

        while esquerda <= direita:
            meio = (esquerda + direita) // 2
            elemento_meio = lista_ordenada[meio]

            if elemento_meio == alvo:
                return meio 
            elif elemento_meio < alvo:
                esquerda = meio + 1
            else:
                direita = meio - 1

        return None


