class Pilha:
    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            print("A pilha está vazia")

    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        else:
            print("A pilha está vazia")

    def tamanho(self):
        return len(self.itens)

# Exemplo de uso:
pilha = Pilha()
pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)

print("Topo da pilha:", pilha.topo())
print("Desempilhando item:", pilha.desempilhar())
print("Topo da pilha:", pilha.topo())
print("Tamanho da pilha:", pilha.tamanho())
