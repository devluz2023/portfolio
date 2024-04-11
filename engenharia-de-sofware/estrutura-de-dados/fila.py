class Fila:
    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def enfileirar(self, item):
        self.itens.append(item)

    def desenfileirar(self):
        if not self.vazia():
            return self.itens.pop(0)
        else:
            print("A fila está vazia")

    def frente(self):
        if not self.vazia():
            return self.itens[0]
        else:
            print("A fila está vazia")

    def tamanho(self):
        return len(self.itens)

# Exemplo de uso:
fila = Fila()
fila.enfileirar(1)
fila.enfileirar(2)
fila.enfileirar(3)

print("Frente da fila:", fila.frente())
print("Desenfileirando item:", fila.desenfileirar())
print("Frente da fila:", fila.frente())
print("Tamanho da fila:", fila.tamanho())
