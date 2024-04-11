class Grafo:
    def __init__(self):
        self.vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.vertices:
            self.vertices[vertice] = []

    def adicionar_aresta(self, origem, destino):
        if origem in self.vertices and destino in self.vertices:
            self.vertices[origem].append(destino)
            # Para um grafo não direcionado, você também precisa adicionar a aresta no sentido contrário
            # self.vertices[destino].append(origem)

    def imprimir_grafo(self):
        for vertice in self.vertices:
            print(vertice, "->", self.vertices[vertice])

# Exemplo de uso:
grafo = Grafo()
grafo.adicionar_vertice('A')
grafo.adicionar_vertice('B')
grafo.adicionar_vertice('C')
grafo.adicionar_vertice('D')

grafo.adicionar_aresta('A', 'B')
grafo.adicionar_aresta('A', 'C')
grafo.adicionar_aresta('B', 'D')
grafo.adicionar_aresta('C', 'D')

grafo.imprimir_grafo()
