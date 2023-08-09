class Passageiros:
    def __init__(self):
        self.Lista_nome_passageiros = []

    def isEmpty(self):
        return self.Lista_nome_passageiros == []

    def adicionar(self, passageiro):
        self.Lista_nome_passageiros = self.Lista_nome_passageiros + [passageiro]

    def deletar(self):
        if not self.isEmpty():
            deleted_item = self.Lista_nome_passageiros[0]
            self.Lista_nome_passageiros = self.Lista_nome_passageiros[1:]
            return deleted_item
        else:
            return None

    def size(self):
        return len(self.nome_passageiros)
    


