class checkout:
    def __init__(self, lista_passageiros):
        self.lista_checkout = lista_passageiros
    
    def isEmpty(self):
        return len(self.lista_checkout) == 0
    
    def empilhar(self, passageiro):
        self.lista_checkout.append(passageiro)

    def desempilhar(self):
        if not self.isEmpty():
            nome_removido = self.lista_checkout[-1]
            self.lista_checkout = self.lista_checkout[:-1]
            return nome_removido
        elif self.isEmpty:
             print(f"O avião já esta vazio")
        
    def head(self):
        if not self.isEmpty():
            return self.lista_checkout[-1]
        elif self.isEmpty:
            print(f"O avião já esta vazio não tem proximo a descer")

    def size(self):
        return len(self.lista_checkout)

